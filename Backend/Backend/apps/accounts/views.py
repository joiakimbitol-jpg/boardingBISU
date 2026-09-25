from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def login_view(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            if not user.is_active:
                messages.error(
                    request,
                    "Your account is currently inactive."
                )

                return render(
                    request,
                    "accounts/login.html"
                )

            login(request, user)

            return redirect("/")

        messages.error(
            request,
            "Invalid email or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


def register_view(request):

    return render(
        request,
        "accounts/register.html"
    )


def logout_view(request):

    logout(request)

    return redirect("/")


def forgot_password_view(request):

    return render(
        request,
        "accounts/forgot_password.html"
    )


def profile_view(request):

    return render(
        request,
        "accounts/profile.html"
    )


def edit_profile_view(request):

    return render(
        request,
        "accounts/edit_profile.html"
    )


def change_password_view(request):

    return render(
        request,
        "accounts/change_password.html"
    )