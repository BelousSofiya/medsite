from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# ROLE_CHOICES = (
#     (0, 'user'),
#     (1, 'admin'),
# )

class CustomUserManager(BaseUserManager):

    def create_user(self, person_email, password=None, **extra_fields):
        person_email = self.normalize_email(person_email)
        user = self.model(
            person_email=person_email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, person_email, password=None, **extra_fields):
        user = self.create_user(person_email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    person_email = models.EmailField(max_length=50, unique=True)
    person_name = models.CharField(max_length=50)
    person_surname = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    USERNAME_FIELD = "person_email"
    EMAIL_FIELD = "person_email"
    REQUIRED_FIELDS = [
        "person_surname",
        "person_name",
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.person_email