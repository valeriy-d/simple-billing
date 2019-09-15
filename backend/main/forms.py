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
