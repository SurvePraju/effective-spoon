from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def home(request):
    form = RegisterUserForm()
    login = LoginUserForm()
    context = {"form": form}
    context["login"] = login
    context["users"] = User.objects.all()
    return render(request, "home.html", context)
