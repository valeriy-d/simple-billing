from django.contrib import admin

from main.models import CountryModel
from main.models import CityModel
from main.models import CurrencyTypeModel
from main.models import CurrencyQuotesModel
from main.models import AccountModel
from main.models import OperationModel
from main.models import TransactionModel


class CurrencyQuotesAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'currency_type', 'usd_exchange_rate']
    list_filter = ['datetime', 'currency_type']


class TransactionInlineAdmin(admin.TabularInline):
    model = TransactionModel
    readonly_fields = [
        'account',
        'type',
        'datetime',
        'currency_rate',
        'amount',
    ]
    # exclude = ['operation']

    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


class OperationAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'type']

    inlines = [TransactionInlineAdmin]


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'account', 'operation', 'type', 'currency_rate', 'amount']
    list_filter = ['datetime', 'account']


admin.site.register(CountryModel)
admin.site.register(CityModel)
admin.site.register(CurrencyTypeModel)
admin.site.register(CurrencyQuotesModel, CurrencyQuotesAdmin)
admin.site.register(AccountModel)
admin.site.register(OperationModel, OperationAdmin)
admin.site.register(TransactionModel, TransactionAdmin)
