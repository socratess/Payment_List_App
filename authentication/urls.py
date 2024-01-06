from django.urls import path
from . import views

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


app_name = 'authentication'

urlpatterns = [
    path("register/", views.register, name="register"),
]
