from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import RegisterForm


def login_view(request):

    # If already logged in, go directly to the correct dashboard
    if request.user.is_authenticated:

        if request.user.role == "student":
            return redirect("dashboard:student")

        elif request.user.role == "owner":
            return redirect("dashboard:owner")

        elif request.user.role == "admin":
            return redirect("dashboard:admin")

        return redirect("home")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            email=email,
            password=password,
        )

        print("LOGIN EMAIL:", email)
        print("USER FOUND:", user)

        if user is not None:

            if not user.is_active:
                messages.error(
                    request,
                    "Your account is currently inactive."
                )

                return render(
                    request,
                    "accounts/login.html",
                    {"email": email},
                )

            login(request, user)

            print("LOGIN SUCCESS")
            print("USER ROLE:", user.role)

            # Send user to the correct dashboard
            if user.role == "student":
                return redirect("dashboard:student")

            elif user.role == "owner":
                return redirect("dashboard:owner")

            elif user.role == "admin":
                return redirect("dashboard:admin")

            messages.error(
                request,
                "Your account has an invalid role."
            )

            logout(request)
            return redirect("accounts:login")

        print("LOGIN FAILED")

        messages.error(
            request,
            "Invalid email or password."
        )

    return render(
        request,
        "accounts/login.html",
        {
            "email": request.POST.get("email", "")
            if request.method == "POST"
            else ""
        },
    )


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            print("REGISTRATION SUCCESS")
            print("REGISTERED EMAIL:", user.email)
            print("REGISTERED ROLE:", user.role)

            messages.success(
                request,
                "Your account has been created successfully. You can now log in."
            )

            return redirect("accounts:login")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def logout_view(request):
    logout(request)
    return redirect("home")


def forgot_password_view(request):
    return render(request, "accounts/forgot_password.html")


def profile_view(request):
    return render(request, "accounts/profile.html")


def edit_profile_view(request):
    return render(request, "accounts/edit_profile.html")


def change_password_view(request):
    return render(request, "accounts/change_password.html")