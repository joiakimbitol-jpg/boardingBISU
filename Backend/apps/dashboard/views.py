from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from apps.accounts.models import User
from .forms import AdminUserCreateForm


@login_required
def student_dashboard(request):
    return render(
        request,
        "dashboard/student_dashboard.html"
    )


@login_required
def owner_dashboard(request):
    return render(
        request,
        "dashboard/owner_dashboard.html"
    )


@login_required
def admin_dashboard(request):
    return render(
        request,
        "dashboard/admin_dashboard.html"
    )


@login_required
def manage_users(request):

    # Only administrators can access User Management
    if request.user.role != User.ADMIN:
        return redirect("home")

    users = User.objects.all().order_by("-date_joined")

    return render(
        request,
        "dashboard/manage_users.html",
        {
            "users": users,
        }
    )


@login_required
def create_user(request):

    # Only administrators can create Owner/Admin accounts
    if request.user.role != User.ADMIN:
        return redirect("home")

    if request.method == "POST":
        form = AdminUserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()

            return redirect("dashboard:manage_users")

    else:
        form = AdminUserCreateForm()

    return render(
        request,
        "dashboard/create_user.html",
        {
            "form": form,
        }
    )