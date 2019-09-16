from django.urls import path
from main.views import RegisterAccountView
from main.views import BalanceRequestView
from main.views import CurrencyUploadView
from main.views import RefillAccountBalanceView
from main.views import TransferMoneyView


urlpatterns = [
    path('register-account/', RegisterAccountView.as_view(), name='register-account'),
    path('<str:username>/balance/', BalanceRequestView.as_view()),
    path('<str:username>/balance/<str:currency>/', BalanceRequestView.as_view()),
    path('balance/refill/', RefillAccountBalanceView.as_view()),
    path('currency/upload/', CurrencyUploadView.as_view()),
    path('transfer-money/', TransferMoneyView.as_view())
]
