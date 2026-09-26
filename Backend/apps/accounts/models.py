from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class User(AbstractUser):
    

    STUDENT = "student"
    OWNER = "owner"
    ADMIN = "admin"

    ROLE_CHOICES = (
        (STUDENT, "Student"),
        (OWNER, "Boarding House Owner"),
        (ADMIN, "Administrator"),
    )

    username = None

    full_name = models.CharField(max_length=150)

    email = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=STUDENT
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(
        default=False
    )
    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.full_name