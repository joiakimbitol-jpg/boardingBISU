from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path("student/", views.student_dashboard, name="student"),
    path("owner/", views.owner_dashboard, name="owner"),
    path("admin/", views.admin_dashboard, name="admin"),
]