from django.db import models

from .user import User


class StudentProfile(models.Model):

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    YEAR_LEVEL_CHOICES = (
        ("1st Year", "1st Year"),
        ("2nd Year", "2nd Year"),
        ("3rd Year", "3rd Year"),
        ("4th Year", "4th Year"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(
        max_length=30,
        unique=True
    )

    course = models.CharField(
        max_length=100
    )

    year_level = models.CharField(
        max_length=20,
        choices=YEAR_LEVEL_CHOICES
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    address = models.TextField()

    emergency_contact = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()} - Student"