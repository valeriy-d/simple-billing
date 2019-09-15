import sys
import logging
from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.db import transaction

from main.models import AccountModel
from main.forms import AccountModelForm
from main.forms import AccountNameForm
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
    def get(self, request, username):
        if not username:
            return JsonResponse({"error": "Username not provided"})

        user = User.objects.filter(username=username)
        if len(user) == 0:
            return JsonResponse({"error": "User not found"})

        user = user[0]
        currency, balance = get_balance(user)
        return JsonResponse({
            "result": {
                "currency": currency,
                "balance": balance
            }
        })
