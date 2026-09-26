from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            full_name="Test User",
            email="test@example.com",
            password="StrongPass123",
        )

    def test_login_view_accepts_email_credentials(self):
        response = self.client.post(
            reverse("accounts:login"),
            {"email": "test@example.com", "password": "StrongPass123"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
