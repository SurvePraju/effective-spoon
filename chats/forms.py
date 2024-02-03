from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]
        widget = {
            "first_name": forms.TextInput(attrs={"class": "form-control"})
        }


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
