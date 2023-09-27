from rest_framework import status
from rest_framework.test import APITestCase

from authentication.factories import CustomUserFactory
from utils.unittest_helper import AnyInt


class UserSelfAPITests(APITestCase):
    def setUp(self):
        self.test_user = CustomUserFactory(
            email="test@test.com",
            name="Test",
            surname="Test",
        )

    def test_user_retrieve_data_successful(self):
        self.test_user.is_staff = True
        self.test_user.save()
        self.client.force_authenticate(self.test_user)
        response = self.client.get(path=f"/api/user/{self.test_user.id}/")
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)
        self.assertEqual(
            {"id": self.test_user.id,
             "email": "test@test.com",
             "name": "Test",
             "surname": "Test"
             },
            response.json()
        )

    def test_user_retrieve_data_not_logged_in(self):
        response = self.client.get(path=f"/api/user/{self.test_user.id}/")
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            {
                "detail": "Authentication credentials were not provided."
            },
            response.json()
        )

    def test_user_update_all_fields_successful(self):
        self.test_user.is_staff = True
        self.test_user.save()
        self.client.force_authenticate(self.test_user)
        response = self.client.put(
            path=f"/api/user/{self.test_user.id}/",
            data={
                "id": AnyInt(),
                "email": "test@test.com",
                "name": "Ivan",
                "surname": "Ivanenko",
            }
        )
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)
        self.assertEqual(
            {"id": AnyInt(),
             "email": "test@test.com",
             "name": "Ivan",
             "surname": "Ivanenko"
             },
            response.json()
        )

    def test_user_update_one_field_successful(self):
        self.test_user.is_staff = True
        self.test_user.save()
        self.client.force_authenticate(self.test_user)
        response = self.client.patch(
            path=f"/api/user/{self.test_user.id}/",
            data={
                "surname": "Petrenko",
            }
        )
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)
        self.assertEqual(
            {"id": AnyInt(),
             "email": "test@test.com",
             "name": "Test",
             "surname": "Petrenko"
             },
            response.json()
        )

    def test_user_update_all_fields_unsuccessful(self):
        self.client.force_authenticate(self.test_user)
        response = self.client.put(
            path=f"/api/user/{self.test_user.id}/",
            data={
                "id": AnyInt(),
                "email": "test@test.com",
                "name": "Ivan",
                "surname": "Ivanenko",
            }
        )
        self.assertEqual(403, response.status_code)

    def test_user_update_one_field_unsuccessful(self):
        self.client.force_authenticate(self.test_user)
        response = self.client.patch(
            path=f"/api/user/{self.test_user.id}/",
            data={"surname": "Petrenko"}
        )
        self.assertEqual(403, response.status_code)


    def test_user_delete(self):
        response = self.client.get(
            path=f"/api/user/{self.test_user.id}/",
        )
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            {"detail": "Authentication credentials were not provided."},
            response.json()
        )
