# Generated by Django 2.2.5 on 2019-09-17 07:01

from django.db import migrations
from django.contrib.auth.models import User


main_auth_user = [
  {
    "id": 1,
    "password": "pbkdf2_sha256$150000$t6tiC44lJGVN$HtJjjggR0tUQeU3fNMkZ5/wgaeCCmSQXeM4jInmYygQ=",
    "last_login": "2019-09-17 07:02:41.068822",
    "is_superuser": 1,
    "username": "root",
    "first_name": "",
    "email": "",
    "is_staff": 1,
    "is_active": 1,
    "date_joined": "2019-09-13 21:01:35.298725",
    "last_name": ""
  },
  {
    "id": 2,
    "password": "pbkdf2_sha256$150000$pjQgYOyBAyX6$xwy2q1/vhe6phQTurC3v1AxcyO45aXY+H5qj4NLKmmk=",
    "last_login": None,
    "is_superuser": 0,
    "username": "jorah",
    "first_name": "Jorah",
    "email": "",
    "is_staff": 0,
    "is_active": 1,
    "date_joined": "2019-09-13 21:03:03",
    "last_name": "Mormont"
  },
  {
    "id": 6,
    "password": "q+HjPXh8X8",
    "last_login": None,
    "is_superuser": 0,
    "username": "gertruda",
    "first_name": "Gertruda",
    "email": "",
    "is_staff": 0,
    "is_active": 1,
    "date_joined": "2019-09-15 09:58:23",
    "last_name": "Heissenberg"
  }
]


main_main_country_model = [
  {
    "id": 1,
    "name": "United States Of America",
    "alias": "USA"
  },
  {
    "id": 3,
    "name": "Canada",
    "alias": "CND"
  }
]


main_main_city_model = [
  {
    "id": 1,
    "name": "New York City",
    "alias": "new_york",
    "country_id": 1
  },
  {
    "id": 2,
    "name": "Toronto",
    "alias": "toronto",
    "country_id": 3
  },
  {
    "id": 3,
    "name": "Ottawa",
    "alias": "ottawa",
    "country_id": 3
  },
  {
    "id": 4,
    "name": "Washington",
    "alias": "washington",
    "country_id": 1
  }
]


main_main_currency_type_model = [
  {
    "id": 1,
    "name": "US Dollar",
    "alias": "USD"
  },
  {
    "id": 2,
    "name": "Euro",
    "alias": "EUR"
  },
  {
    "id": 3,
    "name": "Canadian Dollar",
    "alias": "CAD"
  },
  {
    "id": 4,
    "name": "Chinese Yuan Renminb",
    "alias": "CNY"
  }
]


main_main_currency_quotes_model = [
  {
    "id": 1,
    "usd_exchange_rate": 1.11565,
    "currency_type_id": 2,
    "datetime": "2019-09-15 15:11:01.999758"
  },
  {
    "id": 2,
    "usd_exchange_rate": 0.753463,
    "currency_type_id": 3,
    "datetime": "2019-09-15 15:11:01.999758"
  },
  {
    "id": 3,
    "usd_exchange_rate": 0.141255,
    "currency_type_id": 4,
    "datetime": "2019-09-15 15:11:01.999758"
  },
  {
    "id": 4,
    "usd_exchange_rate": 1,
    "currency_type_id": 1,
    "datetime": "2019-09-15 15:11:01.999758"
  },
  {
    "id": 5,
    "usd_exchange_rate": 1.11443,
    "currency_type_id": 2,
    "datetime": "2019-09-13 15:11:01"
  },
  {
    "id": 6,
    "usd_exchange_rate": 1.114439,
    "currency_type_id": 2,
    "datetime": "2019-09-14 15:11:01"
  },
  {
    "id": 8,
    "usd_exchange_rate": 1.115657,
    "currency_type_id": 2,
    "datetime": "2019-09-15 15:21:23.319048"
  },
  {
    "id": 9,
    "usd_exchange_rate": 1.10691,
    "currency_type_id": 2,
    "datetime": "2019-09-16 05:44:59.712520"
  },
  {
    "id": 10,
    "usd_exchange_rate": 0.755604,
    "currency_type_id": 3,
    "datetime": "2019-09-16 06:03:01.664184"
  }
]


main_main_operation_model = [
  {
    "id": 28,
    "type": 0,
    "datetime": "2019-09-15 16:14:54.690333"
  },
  {
    "id": 29,
    "type": 0,
    "datetime": "2019-09-15 16:14:55.895068"
  },
  {
    "id": 30,
    "type": 0,
    "datetime": "2019-09-15 16:14:56.691277"
  },
  {
    "id": 31,
    "type": 0,
    "datetime": "2019-09-15 16:15:03.475948"
  },
  {
    "id": 32,
    "type": 0,
    "datetime": "2019-09-15 16:15:07.243371"
  },
  {
    "id": 33,
    "type": 0,
    "datetime": "2019-09-15 16:15:11.404774"
  },
  {
    "id": 34,
    "type": 0,
    "datetime": "2019-09-15 16:15:15.370673"
  },
  {
    "id": 35,
    "type": 0,
    "datetime": "2019-09-15 16:15:16.436294"
  },
  {
    "id": 36,
    "type": 1,
    "datetime": "2019-09-15 21:08:01.810380"
  },
  {
    "id": 37,
    "type": 0,
    "datetime": "2019-09-15 21:08:21.129921"
  },
  {
    "id": 38,
    "type": 1,
    "datetime": "2019-09-15 21:08:56.884783"
  },
  {
    "id": 39,
    "type": 1,
    "datetime": "2019-09-16 05:40:24.868575"
  },
  {
    "id": 40,
    "type": 1,
    "datetime": "2019-09-16 06:03:35.989829"
  },
  {
    "id": 41,
    "type": 1,
    "datetime": "2019-09-17 06:22:30.625914"
  },
  {
    "id": 42,
    "type": 1,
    "datetime": "2019-09-17 06:47:53.597793"
  },
  {
    "id": 43,
    "type": 1,
    "datetime": "2019-09-17 06:48:26.433559"
  }
]


main_main_account_model = [
  {
    "id": 1,
    "currency_id": 1,
    "location_id": 1,
    "user_id": 2
  },
  {
    "id": 2,
    "currency_id": 3,
    "location_id": 1,
    "user_id": 6
  }
]


main_main_transaction_model = [
  {
    "id": 27,
    "type": 0,
    "datetime": "2019-09-15 16:14:54.690774",
    "amount": 1,
    "account_id": 2,
    "operation_id": 28,
    "currency_rate_id": 2
  },
  {
    "id": 28,
    "type": 0,
    "datetime": "2019-09-15 16:14:55.895436",
    "amount": 1,
    "account_id": 2,
    "operation_id": 29,
    "currency_rate_id": 2
  },
  {
    "id": 29,
    "type": 0,
    "datetime": "2019-09-15 16:14:56.691734",
    "amount": 1,
    "account_id": 2,
    "operation_id": 30,
    "currency_rate_id": 2
  },
  {
    "id": 30,
    "type": 0,
    "datetime": "2019-09-15 16:15:03.476304",
    "amount": 1,
    "account_id": 2,
    "operation_id": 31,
    "currency_rate_id": 8
  },
  {
    "id": 31,
    "type": 0,
    "datetime": "2019-09-15 16:15:07.243795",
    "amount": 1,
    "account_id": 2,
    "operation_id": 32,
    "currency_rate_id": 4
  },
  {
    "id": 32,
    "type": 0,
    "datetime": "2019-09-15 16:15:11.405170",
    "amount": 1,
    "account_id": 2,
    "operation_id": 33,
    "currency_rate_id": 3
  },
  {
    "id": 33,
    "type": 0,
    "datetime": "2019-09-15 16:15:15.371046",
    "amount": 1,
    "account_id": 2,
    "operation_id": 34,
    "currency_rate_id": 2
  },
  {
    "id": 34,
    "type": 0,
    "datetime": "2019-09-15 16:15:16.436680",
    "amount": 1,
    "account_id": 2,
    "operation_id": 35,
    "currency_rate_id": 2
  },
  {
    "id": 35,
    "type": 1,
    "datetime": "2019-09-15 21:08:01.810884",
    "amount": 6,
    "account_id": 2,
    "operation_id": 36,
    "currency_rate_id": 4
  },
  {
    "id": 36,
    "type": 0,
    "datetime": "2019-09-15 21:08:01.814863",
    "amount": 6,
    "account_id": 1,
    "operation_id": 36,
    "currency_rate_id": 4
  },
  {
    "id": 37,
    "type": 0,
    "datetime": "2019-09-15 21:08:21.130563",
    "amount": 10,
    "account_id": 2,
    "operation_id": 37,
    "currency_rate_id": 2
  },
  {
    "id": 38,
    "type": 1,
    "datetime": "2019-09-15 21:08:56.885192",
    "amount": 9,
    "account_id": 2,
    "operation_id": 38,
    "currency_rate_id": 2
  },
  {
    "id": 39,
    "type": 0,
    "datetime": "2019-09-15 21:08:56.890933",
    "amount": 9,
    "account_id": 1,
    "operation_id": 38,
    "currency_rate_id": 2
  },
  {
    "id": 40,
    "type": 1,
    "datetime": "2019-09-16 05:40:24.868982",
    "amount": 2,
    "account_id": 1,
    "operation_id": 39,
    "currency_rate_id": 2
  },
  {
    "id": 41,
    "type": 0,
    "datetime": "2019-09-16 05:40:24.869383",
    "amount": 2,
    "account_id": 2,
    "operation_id": 39,
    "currency_rate_id": 2
  },
  {
    "id": 42,
    "type": 1,
    "datetime": "2019-09-16 06:03:35.990230",
    "amount": 2,
    "account_id": 1,
    "operation_id": 40,
    "currency_rate_id": 10
  },
  {
    "id": 43,
    "type": 0,
    "datetime": "2019-09-16 06:03:35.990631",
    "amount": 2,
    "account_id": 2,
    "operation_id": 40,
    "currency_rate_id": 10
  },
  {
    "id": 44,
    "type": 1,
    "datetime": "2019-09-17 06:22:30.627176",
    "amount": 2,
    "account_id": 1,
    "operation_id": 41,
    "currency_rate_id": 10
  },
  {
    "id": 45,
    "type": 0,
    "datetime": "2019-09-17 06:22:30.627995",
    "amount": 2,
    "account_id": 2,
    "operation_id": 41,
    "currency_rate_id": 10
  },
  {
    "id": 46,
    "type": 1,
    "datetime": "2019-09-17 06:47:53.598296",
    "amount": 3,
    "account_id": 1,
    "operation_id": 42,
    "currency_rate_id": 3
  },
  {
    "id": 47,
    "type": 0,
    "datetime": "2019-09-17 06:47:53.598774",
    "amount": 3,
    "account_id": 2,
    "operation_id": 42,
    "currency_rate_id": 3
  },
  {
    "id": 48,
    "type": 1,
    "datetime": "2019-09-17 06:48:26.433988",
    "amount": 4,
    "account_id": 2,
    "operation_id": 43,
    "currency_rate_id": 4
  },
  {
    "id": 49,
    "type": 0,
    "datetime": "2019-09-17 06:48:26.438369",
    "amount": 4,
    "account_id": 1,
    "operation_id": 43,
    "currency_rate_id": 4
  }
]


def forward_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    def export(app_name, model_name, collection):
        Model = apps.get_model(app_name, model_name)
        Model.objects.using(db_alias).bulk_create([
            Model(**record) for record in collection
        ])

    # Export Users
    export('auth', 'User', main_auth_user)

    # Export Countries
    export('main', 'CountryModel', main_main_country_model)

    # Export Cities
    export('main', 'CityModel', main_main_city_model)

    # Export Currencies
    export('main', 'CurrencyTypeModel', main_main_currency_type_model)

    # Export Rates
    export('main', 'CurrencyQuotesModel', main_main_currency_quotes_model)

    # Export Accounts
    export('main', 'AccountModel', main_main_account_model)

    # Export Operations
    export('main', 'OperationModel', main_main_operation_model)

    # Export Transactions
    export('main', 'TransactionModel', main_main_transaction_model)


def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    def reverse(app_name, model_name, collection):
        Model = apps.get_model(app_name, model_name)
        for record in collection:
            Model.objects.using(db_alias).filter(**record).delete()

    # Reverse Users
    reverse('auth', 'User', main_auth_user)

    # Reverse Countries
    reverse('main', 'CountryModel', main_main_country_model)

    # Reverse Cities
    reverse('main', 'CityModel', main_main_city_model)

    # Reverse Currencies
    reverse('main', 'CurrencyTypeModel', main_main_currency_type_model)

    # Reverse Rates
    reverse('main', 'CurrencyQuotesModel', main_main_currency_quotes_model)

    # Reverse Accounts
    reverse('main', 'AccountModel', main_main_account_model)

    # Reverse Operations
    reverse('main', 'OperationModel', main_main_operation_model)

    # Reverse Transactions
    reverse('main', 'TransactionModel', main_main_transaction_model)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190915_1511'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func)
    ]
