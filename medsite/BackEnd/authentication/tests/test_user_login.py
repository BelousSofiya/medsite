from rest_framework.test import APITestCase

from authentication.factories import CustomUserFactory
from utils.unittest_helper import AnyStr


class UserLoginAPITests(APITestCase):
    def setUp(self) -> None:
        self.test_person_just_user = CustomUserFactory(
            email="test@user.com",
            password="TTTttt123",
            name="Jane",
            surname="TTT",
        )

    def test_login_just_user(self):
        self.test_person_just_user.set_password("TTTttt123")
        self.test_person_just_user.save()
        response = self.client.post(
            path="/api/token/",
            data={
                "email": "test@user.com",
                "password": "TTTttt123",
            },
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {"access": AnyStr(), "refresh": AnyStr()}, response.json()
        )
        self.assertContains(response, "access")

    #
    def test_login_email_incorrect(self):
        self.test_person_just_user.set_password("TTTttt123")
        self.test_person_just_user.save()

        response = self.client.post(
            path="/api/token/",
            data={
                "email": "tost@user1gbdfg.com",
                "password": "TTTttt123",
            },
        )
        self.assertEqual(401, response.status_code)
        self.assertEqual(
            {"detail": "No active account found with the given credentials"},
            response.json(),
        )

    def test_login_password_incorrect(self):
        self.test_person_just_user.set_password("Test1234")
        self.test_person_just_user.save()

        response = self.client.post(
            path="/api/token/",
            data={
                "email": "test@user.com",
                "password": "Test5678",
            },
        )
        self.assertEqual(401, response.status_code)
        self.assertEqual(
            {"detail": "No active account found with the given credentials"},
            response.json(),
        )
