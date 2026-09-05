from django.shortcuts import render


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def logout_view(request):
    pass


def forgot_password_view(request):
    return render(request, "accounts/forgot_password.html")


def profile_view(request):
    return render(request, "accounts/profile.html")


def edit_profile_view(request):
    return render(request, "accounts/edit_profile.html")


def change_password_view(request):
    return render(request, "accounts/change_password.html")