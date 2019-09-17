import csv
import logging
from dicttoxml import dicttoxml

from django.views import View
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.db.models import F
from django.db.models import Case, When
from django.db.models import CharField
from django.db.models import Value as V

from main.models import AccountModel
from main.models import OperationModel
from main.models import TransactionModel
from main.models import CurrencyTypeModel


logger = logging.getLogger('main')


class BaseReport:
    return_fields = [
        "op_id",
        "transaction_id",
        "currency_alias",
        "usd_exchange_rate",
        "op_type",
        "transaction_type",
        "transaction_datetime",
    ]

    def get_data(self, request, username, date_from, date_to=None):
        # Ищем счет
        try:
            account = AccountModel.objects.select_related('user').get(user__username=username)
        except AccountModel.DoesNotExist as e:
            return JsonResponse({"error": "User not found"}, status=400)

        # Получим все операции с транзакциями юзера
        account_transactions = TransactionModel.objects\
            .select_related("operation", "currency_rate")\
            .filter(account=account)

        if date_to is not None:
            logger.debug(date_to)
            date_to = date_to.replace(day=date_to.day + 1)
            logger.debug(date_to)
            account_transactions = account_transactions.filter(
                datetime__gte=date_from,
                datetime__lt=date_to
            )
        else:
            account_transactions = account_transactions.filter(
                datetime__gte=date_from
            )

        dc = dict(TransactionModel.TRN_TYPE)
        account_transactions = account_transactions.annotate(
            transaction_id=F("pk"),
            transaction_type=Case(
                When(type=TransactionModel.DEBIT, then=V(dc[TransactionModel.DEBIT])),
                When(type=TransactionModel.CREDIT, then=V(dc[TransactionModel.CREDIT])),
                default="type",
                output_field=CharField(),
            ),
            op_id=F("operation__pk"),
            op_type=Case(
                When(operation__type=OperationModel.REFILL, then=V("refill")),
                When(operation__type=OperationModel.TRANSFER, then=V("transfer")),
                default="type",
                output_field=CharField(),
            ),
            currency_alias=F("currency_rate__currency_type__alias"),
            usd_exchange_rate=F("currency_rate__usd_exchange_rate"),
            transaction_datetime=F("datetime")
        ).values(
            "op_id",
            "transaction_id",
            "currency_alias",
            "usd_exchange_rate",
            "op_type",
            "amount",
            "transaction_type",
            "transaction_datetime",
        )

        return account_transactions


class UserReportView(BaseReport, View):
    def get(self, request, username, date_from, date_to=None):

        account_transactions = self.get_data(request, username, date_from, date_to)
        if isinstance(account_transactions, JsonResponse):
            return account_transactions

        logger.debug(account_transactions.query)

        return JsonResponse({"result": [a for a in account_transactions]})


class UserReportCSVView(BaseReport, View):
    def get(self, request, username, date_from, date_to=None):
        account_transactions = self.get_data(request, username, date_from, date_to)
        if isinstance(account_transactions, JsonResponse):
            return account_transactions

        response = HttpResponse(content_type='text/csv')
        filename = f"{username}_report.csv"
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
        writer = csv.writer(
            response,
            delimiter=';',
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        writer.writerow(self.return_fields)

        for t in account_transactions.values_list(*self.return_fields):
            writer.writerow(t)

        return response


class UserReportXMLView(BaseReport, View):
    def get(self, request, username, date_from, date_to=None):

        account_transactions = self.get_data(request, username, date_from, date_to)
        if isinstance(account_transactions, JsonResponse):
            return account_transactions

        xml = dicttoxml(account_transactions, attr_type=False)
        response = HttpResponse(xml, content_type='text/xml')
        filename = f"{username}_report.xml"
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)

        return response
