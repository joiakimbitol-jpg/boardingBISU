from django import forms
from django.contrib.auth.password_validation import validate_password

from apps.accounts.models import User
from apps.accounts.models.user import UserRole


class StudentRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )

    def clean_email(self):

        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists."
            )

        return email

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:

            raise forms.ValidationError(
                "Passwords do not match."
            )

        validate_password(password)

        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)

        user.role = UserRole.STUDENT

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user