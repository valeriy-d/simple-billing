from django.db import models
from django.contrib.auth.models import User


class CountryModel(models.Model):
    name = models.CharField("Country name", max_length=255)
    alias = models.CharField("Short alias", max_length=5)

    def __str__(self):
        return f"{self.alias} - {self.name}"


class CityModel(models.Model):
    name = models.CharField("City name", max_length=255)
    alias = models.CharField("Short alias", max_length=20)
    country = models.ForeignKey(CountryModel, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.country}"


class CurrencyTypeModel(models.Model):
    name = models.CharField("Currency name", max_length=20)
    alias = models.CharField("Currency alias", max_length=5)

    def __str__(self):
        return f"{self.alias} - {self.name}"


class CurrencyQuotesModel(models.Model):
    currency_type = models.ForeignKey(CurrencyTypeModel, on_delete=models.PROTECT)
    usd_exchange_rate = models.DecimalField("USD exchange rate", max_digits=16, decimal_places=6)


class AccountModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    currency = models.ForeignKey(CurrencyTypeModel, on_delete=models.PROTECT)
    location = models.ForeignKey(CityModel, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}; {self.currency.alias}; {self.location.name}"


class OperationModel(models.Model):
    REFILL = 0
    TRANSFER = 1

    OP_TYPE = [
        (REFILL, 'refill'),
        (TRANSFER, 'transfer'),
    ]

    type = models.IntegerField("Transaction type", choices=OP_TYPE)
    datetime = models.DateTimeField("Operation datetime")


class TransactionModel(models.Model):
    DEBIT = 0
    CREDIT = 1

    TRN_TYPE = [
        (DEBIT, 'debit'),
        (CREDIT, 'credit')
    ]

    account = models.ForeignKey(AccountModel, on_delete=models.PROTECT)
    operation = models.ForeignKey(OperationModel, on_delete=models.PROTECT)
    type = models.IntegerField("Transaction type", choices=TRN_TYPE)
    datetime = models.DateTimeField("Transaction datetime")
    currency = models.ForeignKey(CurrencyTypeModel, on_delete=models.PROTECT)
    exchange_quote = models.DecimalField("USD exchange rate",
                                         max_digits=16,
                                         decimal_places=6,
                                         help_text="The USD exchange rate on operation moment")
    amount = models.IntegerField("Operations amount")