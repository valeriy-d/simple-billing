from django.urls import path
from main.views import RegisterAccountView
from main.views import BalanceRequestView


urlpatterns = [
    path('register-account/', RegisterAccountView.as_view(), name='register-account'),
    path('<str:username>/balance/', BalanceRequestView.as_view())
]
