from django.contrib.auth.models import User
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"
        pass
