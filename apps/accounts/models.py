from django.db import models

# Create your models here.
class UserRole(models.TextChoices):
    STUDENT = 'student', 'Student'
    OWNER = 'owner', 'Boarding House Owner'
    ADMIN = 'admin', 'Administrator'