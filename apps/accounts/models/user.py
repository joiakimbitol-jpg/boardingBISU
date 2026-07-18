from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.managers.user_manager import UserManager


class UserRole(models.TextChoices):
    STUDENT = "student", "Student"
    OWNER = "owner", "Boarding House Owner"
    ADMIN = "admin", "Administrator"


class User(AbstractUser):

    email = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STUDENT
    )

    profile_picture = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    objects = UserManager()

    REQUIRED_FIELDS = [
        "email"
    ]

    def __str__(self):
        return self.username