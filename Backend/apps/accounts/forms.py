from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = (
            "full_name",
            "email",
            "phone_number",
            "password1",
            "password2",
        )

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full Name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address",
            }),

            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number",
            }),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password",
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm Password",
        })
    )

    def save(self, commit=True):
        user = super().save(commit=False)

        # Public registration is always Student
        user.role = User.STUDENT

        if commit:
            user.save()

        return user