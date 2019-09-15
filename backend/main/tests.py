import json
import pytest

from functools import partial
from django.test import Client
from django.contrib.auth.models import User

from main.models import CurrencyTypeModel
from main.models import CountryModel
from main.models import CityModel
from main.models import AccountModel


JSON = "application/json"


class RegistrAccountTestCase:
    def setup(self):
        # Создадим валюту
        self.currency = CurrencyTypeModel(name="USD Dollar", alias="USD")
        self.currency.save()

        # Создадим страну и город
        self.country = CountryModel(name="USA", alias="USA")
        self.country.save()

        self.city = CityModel(name="New York City", alias="New York", country=self.country)
        self.city.save()

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
        res = c.post('/register-account', data=data, content_type=JSON)

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

        res = c.post('/register-account', data=data, content_type=JSON)

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
            "currency": self.country.pk,
            "location": self.currency.pk
        }

        res = c.post('/register-account', data=data, content_type=JSON)
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
