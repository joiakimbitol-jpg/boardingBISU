from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from apps.accounts.forms import (
    LoginForm,
    StudentRegistrationForm,
    OwnerRegistrationForm,
)
from apps.accounts.models.user import UserRole

def student_register_view(request):

    if request.method == "POST":

        form = StudentRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student account created successfully."
            )

            return redirect("login")

    else:

        form = StudentRegistrationForm()

    return render(
        request,
        "accounts/register_student.html",
        {
            "form": form
        }
    )

# Owner View
def owner_register_view(request):

    if request.method == "POST":

        form = OwnerRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Owner account created successfully."
            )

            return redirect("login")

    else:

        form = OwnerRegistrationForm()

    return render(
        request,
        "accounts/register_owner.html",
        {
            "form": form
        }
    )
#Login View
def login_view(request):

    if request.user.is_authenticated:

        return redirect("home")

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                if user.role == UserRole.ADMIN:
                    return redirect("admin_dashboard")

                elif user.role == UserRole.OWNER:
                    return redirect("owner_dashboard")

                return redirect("student_dashboard")

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )
#Logout View
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("login")