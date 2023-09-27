from collections import defaultdict
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
# from djoser.serializers import UserCreatePasswordRetypeSerializer, UserSerializer, TokenCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from validation.validate_password import validate_password_length, validate_password_include_symbols
from authentication.models import CustomUser

# User = get_user_model()


# class UserRegistrationSerializer(UserCreatePasswordRetypeSerializer):
#     email = serializers.EmailField(write_only=True, validators=[UniqueValidator(
#         queryset=User.objects.all(), message="Email is already registered")])
#     password = serializers.CharField(
#         style={"input_type": "password"}, write_only=True)
#
#     class Meta(UserCreatePasswordRetypeSerializer.Meta):
#         model = User
#         fields = (
#             "email",
#             "password",
#             "name",
#             "surname",
#         )
#
class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
                    "email",
                    "password",
                    "name",
                    "surname",
                )

    def validate(self, value):
        custom_errors = defaultdict(list)
        password = value.get("password")
        try:
            validate_password_length(password)
        except ValidationError as error:
            custom_errors["password"].append(error.message)
        try:
            validate_password_include_symbols(password)
        except ValidationError as error:
            custom_errors["password"].append(error.message)
        if custom_errors:
            raise serializers.ValidationError(custom_errors)
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "name",
            "surname",
        )
