import sys
import logging
from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.db import transaction
from django.utils import timezone

from main.models import AccountModel
from main.models import CurrencyTypeModel
from main.models import CurrencyQuotesModel
from main.models import OperationModel
from main.models import TransactionModel
from main.forms import AccountModelForm
from main.forms import AccountNameForm
from main.forms import CurrencyUploadForm
from main.forms import AccountRefillForm
from utils.decorators import json_required
from utils.auth import gen_password
from main.commands import get_balance


logger = logging.getLogger('main')


class RegisterAccountView(View):
    @json_required
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.json

        # Проверяем, что есть все поля для создания юзера
        form = AccountNameForm(data)
        if not form.is_valid():
            transaction.set_rollback(True)
            return JsonResponse({"error": form.errors}, status=400)

        # Генерируем пароль и создаем юзера
        password = gen_password()
        user = User(**form.cleaned_data, password=password)
        user.save()
        data['user'] = user.pk

        # Проверяем, что остальные даные так же корректны
        form = AccountModelForm(data)
        if not form.is_valid():
            transaction.set_rollback(True)
            return JsonResponse({"error": form.errors}, status=400)

        # Создаем окончательный счет для пользователя
        account = AccountModel(**form.cleaned_data)
        account.save()

        return JsonResponse({
            "username": account.user.username,
            "password": password,
            "currency": account.currency.alias,
        })


class BalanceRequestView(View):
    def get(self, request, username, currency=None):
        if not username:
            return JsonResponse({"error": "Username not provided"})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist as e:
            return JsonResponse({"error": "User not found"})

        if currency:
            try:
                currency = CurrencyTypeModel.objects.get(alias=currency.upper())
            except CurrencyTypeModel.DoesNotExist as e:
                return JsonResponse({"error": "Currency does not exist"})

        currency, balance = get_balance(user, currency)
        return JsonResponse({
            "result": {
                "currency": currency,
                "balance": balance
            }
        })


class CurrencyUploadView(View):
    @json_required
    def post(self, request):
        data = request.json

        form = CurrencyUploadForm(data)

        if not form.is_valid():
            return JsonResponse(form.errors, status=400)

        data = form.cleaned_data
        currency_alias, rate = data['currency'], data['usd_exchange_rate']

        try:
            currency = CurrencyTypeModel.objects.get(alias=currency_alias.upper())
        except CurrencyTypeModel.DoesNotExist as e:
            return JsonResponse({"error": "Currency does not exist"})

        new_rate = CurrencyQuotesModel(currency_type=currency, usd_exchange_rate=rate, datetime=timezone.now())
        new_rate.save()

        return JsonResponse({
            "result": {
                "currency": currency.alias,
                "usd_exchange_rate": rate,
                "datetime": new_rate.datetime
            }
        })


class RefillAccountBalanceView(View):
    @json_required
    @transaction.atomic
    def post(self, request):
        data = request.json
        form = AccountRefillForm(data)

        if not form.is_valid():
            return JsonResponse({"error": form.errors})

        data = form.cleaned_data
        currency_alias, amount, username = data['currency'], data['amount'], data['username']

        # Ищем счет
        try:
            account = AccountModel.objects.select_related('user').get(user__username=username)
        except AccountModel.DoesNotExist as e:
            return JsonResponse({"error": "User not found"})

        data = form.cleaned_data
        currency_alias, amount = data['currency'], data['amount']

        # Ищем последнюю актуальную котировку для заданной валюты
        try:
            currency = CurrencyQuotesModel.objects\
                .select_related('currency_type')\
                .filter(currency_type__alias=currency_alias.upper()).latest('datetime')
        except CurrencyQuotesModel.DoesNotExist as e:
            return JsonResponse({"error": "Currency does not exist"})

        # Создаем операцию
        operation = OperationModel(type=OperationModel.REFILL, datetime=timezone.now())
        operation.save()

        # Создаем транзакцию
        debit_transaction = TransactionModel(
            account=account,
            operation=operation,
            type=TransactionModel.DEBIT,
            datetime=timezone.now(),
            currency_rate=currency,
            amount=amount
        )
        debit_transaction.save()

        user_currency, balance = get_balance(account.user)
        return JsonResponse({
            "result": {
                "refill_amount": amount,
                "current_balance": balance,
                "currency": user_currency
            }
        })
