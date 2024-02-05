from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from . import forms

# Create your views here.


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        forms.User(username=username, password=password1).save()

        return redirect("login")
    else:
        form = forms.RegisterUserForm()
        context = {"form": form}
        return render(request, "register.html", context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    else:
        return redirect("login")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")
    else:
        form = forms.LoginUserForm()
        context = {}
        context["form"] = form
        return render(request, "login.html", context)
