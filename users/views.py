
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .forms import ProfileForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")

        messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm(request)

    return render(request, "users/login.html", {"form": form})


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        messages.success(request, "You have logged out successfully!")
        return redirect("login")

    return redirect("home")


@login_required
def profile(request):
    return render(request, "users/profile.html")


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your profile has been updated."
            )
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "users/edit_profile.html",
        {"form": form}
    )
