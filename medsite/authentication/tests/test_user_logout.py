from rest_framework import status
from rest_framework.test import APITestCase

from authentication.factories import CustomUserFactory


class UserLogoutAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUserFactory(email="test@test.com")

    def test_logout_successful(self):
        self.user.set_password("Test12345")
        self.user.save()

        self.test_user_token = self.client.post(
            path="/api/token/",
            data={
                "email": "test@test.com",
                "password": "Test12345",
            },
        ).data
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.test_user_token['access']}"
        )
        response = self.client.post(
            path="/api/logout/", data={"refresh": self.test_user_token["refresh"]}
        )
        self.assertEqual(205, response.status_code)

    #
    def test_logout_not_logged_in(self):
        response = self.client.post(path="/api/logout/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            {"detail": "Authentication credentials were not provided."}, response.json()
        )
