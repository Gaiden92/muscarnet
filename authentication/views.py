from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from .form import RegisterForm, LoginForm


def registration_view(request):
    message = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription confirmé.")
            return redirect("login-page")
    else:
        form = RegisterForm()

    return render(request, "registration.html", {"form": form})


def login_view(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
        if user is not None:
            login(request, user)
            return redirect("dashboard-page", user.id)
        else:
            message = "Identifants invalides !"
    else:
        form = LoginForm()

    return render(request, "index.html", {"form": form, "message": message})



def logout_view(request):
    logout(request)
    return redirect("index-page")
