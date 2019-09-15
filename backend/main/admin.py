from django.contrib import admin

from main.models import CountryModel
from main.models import CityModel
from main.models import CurrencyTypeModel
from main.models import CurrencyQuotesModel
from main.models import AccountModel
from main.models import OperationModel
from main.models import TransactionModel


admin.site.register(CountryModel)
admin.site.register(CityModel)
admin.site.register(CurrencyTypeModel)
admin.site.register(CurrencyQuotesModel)
admin.site.register(AccountModel)
admin.site.register(OperationModel)
admin.site.register(TransactionModel)
