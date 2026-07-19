from django.urls import path

from apps.accounts.views import (
    login_view,
    logout_view,
    student_register_view,
    owner_register_view,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/student/", student_register_view, name="register_student"),
    path("register/owner/", owner_register_view, name="register_owner"),
]