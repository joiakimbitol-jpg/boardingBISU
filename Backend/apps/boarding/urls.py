from django.urls import path
from . import views


app_name = "boarding"


urlpatterns = [
    path("", views.boarding_houses, name="boarding_houses"),
]