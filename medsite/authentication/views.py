from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, TokenError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from authentication.models import CustomUser
from authentication.serializers import CustomUserRegistrationSerializer, CustomUserListSerializer


class CustomUserRegistrationView(CreateAPIView):
    serializer_class = CustomUserRegistrationSerializer
    queryset = CustomUser.objects.all()


class CustomUserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserListSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAdminUser,)


class CustomUserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response(status.HTTP_400_BAD_REQUEST)

