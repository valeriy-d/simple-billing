from django.urls import path
from main.views import RegisterAccountView


urlpatterns = [
    path('register-account', RegisterAccountView.as_view(), name='register-account'),
]
