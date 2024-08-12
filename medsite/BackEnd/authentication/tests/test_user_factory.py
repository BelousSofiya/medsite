from django.test import TestCase

from authentication.factories import CustomUserFactory


class TestFactories(TestCase):
    def test_user_factory(self):
        user = CustomUserFactory()
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.name)
        self.assertIsNotNone(user.surname)
