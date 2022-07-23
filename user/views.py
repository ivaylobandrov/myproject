from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm, UserUpdateForm


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


def me(request, pk):
    user = User.objects.get(id=pk)
    form = UserUpdateForm(instance=user)

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("gallery")

    context = {"form": form}
    return render(request, "me.html", context)
