from django import forms
from main.models import AccountModel


class AccountNameForm(forms.Form):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    username = forms.CharField(max_length=256)


class AccountModelForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = ['user', 'currency', 'location']


class CurrencyUploadForm(forms.Form):
    currency = forms.CharField(max_length=5)
    usd_exchange_rate = forms.DecimalField(max_digits=16, decimal_places=6)


class AccountRefillForm(forms.Form):
    currency = forms.CharField(max_length=5)
    amount = forms.DecimalField(max_digits=16, decimal_places=6)
    username = forms.CharField(max_length=256)
