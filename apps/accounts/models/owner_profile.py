from django.db import models

from .user import User


class VerificationStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    REJECTED = "rejected", "Rejected"


class OwnerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="owner_profile"
    )

    business_name = models.CharField(
        max_length=150
    )

    government_id = models.ImageField(
        upload_to="government_ids/"
    )

    phone_number = models.CharField(
        max_length=15
    )

    address = models.TextField()

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.business_name