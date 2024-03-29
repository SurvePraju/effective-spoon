from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1"]


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
