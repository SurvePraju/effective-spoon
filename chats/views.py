from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    context = {}
    context["users"] = User.objects.all()
    return render(request, "home.html", context)


def room(request, username):
    context = {"username": username, "users": User.objects.all()}
    return render(request, "home.html", context)
