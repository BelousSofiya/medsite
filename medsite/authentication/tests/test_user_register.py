from rest_framework import status
from rest_framework.test import APITestCase

from authentication.factories import CustomUserFactory
from authentication.models import CustomUser


class UserRegistrationAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUserFactory(email="test@test.com")

    def test_register_user_successful(self):
        response = self.client.post(
            path="/api/registration/",
            data={
                "email": "jane@test.com",
                "password": "Test1234",
                "re_password": "Test1234",
                "name": "Jane",
                "surname": "Smith",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            "jane@test.com",
            response.json()["email"],
        )
        self.assertEqual(CustomUser.objects.get(name="Jane").email, "jane@test.com")
        self.assertEqual(CustomUser.objects.get(email="jane@test.com").name, "Jane")

    def test_register_user_email_incorrect(self):
        response = self.client.post(
            path="/api/registration/",
            data={
                "email": "jane@testcom",
                "password": "Test1234",
                "re_password": "Test1234",
                "name": "Jane",
                "surname": "Smith",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {"email": ["Enter a valid email address."]},
            response.json(),
        )

    def test_register_user_email_exists(self):
        response = self.client.post(
            path="/api/registration/",
            data={
                "email": "test@test.com",
                "password": "Test1234",
                "re_password": "Test1234",
                "name": "Test",
                "surname": "Test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {"email": ["custom user with this email already exists."]},
            response.json(),
        )

    def test_register_user_password_incorrect(self):
        response = self.client.post(
            path="/api/registration/",
            data={
                "email": "jane@test.com",
                "password": "test",
                "re_password": "tess",
                "name": "Jane",
                "surname": "Smith",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {
                "password": [
                    "Password must be at least 8 characters long.",
                    "Password must include at least one uppercase letter (A-Z), one lowercase letter (a-z) and "
                    "one digit (0-9).",
                ]
            },
            response.json(),
        )

    def test_register_user_who_represent_empty_fields(self):
        response = self.client.post(
            path="/api/registration/",
            data={
                "email": "jane@test.com",
                "password": "Test1234",
                "name": "Jane",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {"surname": ["This field is required."]},
            response.json(),
        )
