from django.urls import path
from . import views


app_name = "dashboard"


urlpatterns = [
    path(
        "student/",
        views.student_dashboard,
        name="student"
    ),

    path(
        "owner/",
        views.owner_dashboard,
        name="owner"
    ),

    path(
        "admin/",
        views.admin_dashboard,
        name="admin"
    ),

    path(
        "admin/users/",
        views.manage_users,
        name="manage_users"
    ),

    path(
        "admin/users/create/",
        views.create_user,
        name="create_user"
    ),
]