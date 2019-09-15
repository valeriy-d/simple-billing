import logging
from decimal import Decimal

from main.models import AccountModel
from main.models import TransactionModel
from main.models import CurrencyTypeModel
from main.models import CurrencyQuotesModel



logger = logging.getLogger('main')


def get_balance(user, requested_currency=None):
    account = AccountModel.objects.get(user=user)

    # Получим все транзакции для счета
    all_trns = TransactionModel.objects.filter(account=account)

    for t in all_trns:
        if not t.type == TransactionModel.DEBIT:
            continue

    # Сумма дебита в USD
    sum_debit = sum([t.amount * t.currency_rate.usd_exchange_rate
                     for t in all_trns
                     if t.type == TransactionModel.DEBIT])

    # Сумма кредита в USD
    sum_credit = sum([t.amount * t.currency_rate.usd_exchange_rate
                     for t in all_trns
                     if t.type == TransactionModel.CREDIT])

    logger.debug(sum_debit)
    logger.debug(sum_credit)

    # Получим актуальный рейт запрошенной или родной валюты
    currency = account.currency
    if requested_currency:
        currency = requested_currency

    rate = CurrencyQuotesModel.objects.filter(currency_type=currency).latest('datetime')

    return currency.alias, ((sum_debit - sum_credit) / rate.usd_exchange_rate).quantize(Decimal("1.000000"))
