import json
import pytest
from decimal import Decimal

from django.test import Client
from django.utils import timezone
from django.contrib.auth.models import User

from utils.auth import gen_password
from main.commands import get_balance

from main.models import CurrencyTypeModel
from main.models import CurrencyQuotesModel
from main.models import CountryModel
from main.models import CityModel
from main.models import AccountModel
from main.models import OperationModel
from main.models import TransactionModel


JSON = "application/json"


class BaseTestCls:
    def refill(self, account, rate, amount):
        op = OperationModel.objects.create(type=OperationModel.REFILL, datetime=timezone.now())
        debit_transaction = TransactionModel(
            account=account,
            operation=op,
            type=TransactionModel.DEBIT,
            datetime=timezone.now(),
            currency_rate=rate,
            amount=amount
        )
        debit_transaction.save()

    def setup(self):
        # Создадим валюту
        self.currency = CurrencyTypeModel(name="USD Dollar", alias="USD")
        self.currency.save()

        self.currency_eur = CurrencyTypeModel(name="Euro", alias="EUR")
        self.currency_eur.save()

        self.currency_cad = CurrencyTypeModel(name="Canadian Dollar", alias="CAD")
        self.currency_cad.save()

        # Добавим котировки
        self.rate_usd = CurrencyQuotesModel.objects.create(
            currency_type=self.currency,
            usd_exchange_rate=Decimal("1.0"),
            datetime=timezone.now()
        )
        self.rate_cad = CurrencyQuotesModel.objects.create(
            currency_type=self.currency_cad,
            usd_exchange_rate=Decimal("0.753463"),
            datetime=timezone.now()
        )
        self.rate_eur = CurrencyQuotesModel.objects.create(
            currency_type=self.currency_eur,
            usd_exchange_rate=Decimal("1.106910"),
            datetime=timezone.now()
        )

        # Создадим страну и город
        self.country = CountryModel(name="USA", alias="USA")
        self.country.save()

        self.city = CityModel(name="New York City", alias="New York", country=self.country)
        self.city.save()

        # Создадим пользователя и счет
        self.user1 = User(username="test_user_1", password=gen_password())
        self.user1.save()
        self.account1 = AccountModel(user=self.user1, currency=self.currency_cad, location=self.city)
        self.account1.save()

        self.user2 = User(username="test_user_2", password=gen_password())
        self.user2.save()
        self.account2 = AccountModel(user=self.user2, currency=self.currency_eur, location=self.city)
        self.account2.save()


class RegistrAccountTestCase(BaseTestCls):
    @pytest.mark.django_db(transaction=True)
    def test_register_account_bad_userdata(self):
        """
        Проверяем, что если не передали данных для создания юзере,
        то будет ошибка
        """
        c = Client()
        data = {
            "first_name": "John",
            "username": "john",
            "currency": 0,
            "location": 0
        }
        res = c.post('/register-account/', data=data, content_type=JSON)

        assert res.status_code == 400, f"Bad HTTP Status Code expected 400, got {res.status_code}"

    @pytest.mark.django_db(transaction=True)
    def test_register_account_bad_account_data(self):
        """
        Проверяем, что если не верные данные для счета, то счет не создается
        """
        c = Client()
        data = {
            "last_name": "Sandman",
            "first_name": "John",
            "username": "san_john",
            "currency": 999,
            "location": 999
        }

        res = c.post('/register-account/', data=data, content_type=JSON)

        assert res.status_code == 400, f"Bad HTTP Status Code expected 400, got {res.status_code}"
        jres = json.loads(res.content)

        got_list = set(jres['error'].keys())
        wrong_list = {'currency', 'location'}

        assert not (got_list ^ wrong_list), \
            f"Wrong fields list expected {wrong_list} got {got_list}"

    @pytest.mark.django_db(transaction=True)
    def test_register_account_success(self):
        """
        Проверяем, что при корректных переданных данных,
        счет создается корректно и ответ в правильном формате
        """
        c = Client()

        data = {
            "last_name": "Sandman",
            "first_name": "John",
            "username": "san_john",
            "currency": self.currency.pk,
            "location": self.country.pk
        }

        res = c.post('/register-account/', data=data, content_type=JSON)
        assert res.status_code == 200, f"Bad HTTP Status Code expected 200 got {res.status_code}"

        jres = json.loads(res.content)

        got_fields = set(jres.keys())
        expected_fields = {'username', 'password', 'currency'}

        # Проверим формат ответа
        assert not (got_fields ^ expected_fields), \
            f"Wrong field list expected {expected_fields} got {got_fields}"

        # Теперь проверим, что создан пользователь и счет
        # Попытаемся найти созданного пользователя
        user = User.objects.filter(username=data['username'])
        assert len(user) == 1, f"User has not been created"

        # Проверяем, что создан счет
        user = user[0]
        account = AccountModel.objects.filter(user=user)

        assert len(account) == 1, f"Account has not been created"


class BalanceRequestTestCase(BaseTestCls):
    def setup(self):
        super().setup()

        # Создадим операцию пополнения
        # чтобы на балансе были средства
        self.refill(self.account1, self.rate_cad, 100)

    @pytest.mark.django_db(transaction=True)
    def test_get_balance(self):
        _, balance = get_balance(self.user1)

        assert balance == 100, f"Balance incorrect, expected 100 got {balance}"

        # Добавим операцию и проверим, что баланс изменился
        self.refill(self.account1, self.rate_cad, 10)

        _, balance = get_balance(self.user1)
        assert 110 == balance, f"Balance incorrect, expected 110 got {balance}"

    @pytest.mark.django_db(transaction=True)
    def test_user_not_provided(self):
        c = Client()

        res = c.get(f"/user_not_exist/balance/")

        assert res.status_code == 400, f"Bad HTTP Response Code, expected 400, got {res.status_code}"

    @pytest.mark.django_db(transaction=True)
    def test_currency_not_found(self):
        c = Client()

        res = c.get(f"/{self.user1.username}/balance/byr/")
        assert res.status_code == 400, f"Bad HTTP Response Code, expected 400, got {res.status_code}"

    @pytest.mark.django_db(transaction=True)
    def test_success_balance(self):
        c = Client()

        res = c.get(f"/{self.user1.username}/balance/")
        assert res.status_code == 200, f"Bad HTTP Response Code, expected 200, got {res.status_code}"

        jres = json.loads(res.content)

        assert jres['result']['currency'] == 'CAD', \
            f"Wrong returning currency, expected CAD, got {jres['result']['currency']}"

        got_balance = Decimal(jres['result']['balance']).quantize(Decimal("1.000000"))
        expected_balance = Decimal("100").quantize(Decimal("1.000000"))

        assert got_balance == expected_balance, \
            f"Balance incorrect, expected 100, got {jres['result']['balance']}"


class CurrencyUploadTestCase(BaseTestCls):
    @pytest.mark.django_db(transaction=True)
    def test_bad_params(self):
        c = Client()

        data = {
            "currency": "byr",
            "usd_exchange_rate": 0.755604
        }

        res = c.post('/currency/upload/', data=data, content_type=JSON)

        assert res.status_code == 400,\
            f"Bad HTTP Response Code, expected 400, got {res.status_code}"

        jres = json.loads(res.content)
        assert jres['error'] == "Currency does not exist", f"Wrong error text"

    @pytest.mark.django_db(transaction=True)
    def test_success_currency_upload(self):
        c = Client()

        data = {
            "currency": "cad",
            "usd_exchange_rate": 0.755604
        }

        res = c.post('/currency/upload/', data=data, content_type=JSON)

        assert res.status_code == 200,\
            f"Bad HTTP Response Code, expected 200, got {res.status_code}"

        jres = json.loads(res.content)
        last_cad = CurrencyQuotesModel.objects\
            .select_related('currency_type')\
            .filter(currency_type=self.currency_cad)\
            .latest("datetime")

        assert Decimal(jres['result']['usd_exchange_rate']) == last_cad.usd_exchange_rate \
            and jres['result']['currency'] == last_cad.currency_type.alias, \
            f"Wrong answer from server"
