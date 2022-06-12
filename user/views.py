from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def user_login(request):

    if request.user.is_authenticated:
        return redirect("gallery")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            "Hello"
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET["next"] if "next" in request.GET else "gallery")
        else:
            "Hello"

    return render(request, "login.html")


def register_user(request):

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            login(request, user)
            return redirect("gallery")

    context = {"form": form}
    return render(request, "register.html", context)


def logout_user(request):
    logout(request)
    return redirect("gallery")
