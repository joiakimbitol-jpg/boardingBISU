from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import (
    User,
    StudentProfile,
    OwnerProfile
)
from apps.accounts.models.user import UserRole


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        if instance.role == UserRole.STUDENT:

            StudentProfile.objects.create(
                user=instance,
                student_id="",
                course="",
                year_level="1st Year",
                gender="Male",
                address="",
                emergency_contact=""
            )

        elif instance.role == UserRole.OWNER:

            OwnerProfile.objects.create(
                user=instance,
                business_name="",
                phone_number="",
                address=""
            )