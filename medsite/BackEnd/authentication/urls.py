from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from authentication.views import (
    CustomUserRegistrationView,
    CustomUserDetailView,
    CustomUserLogoutView,
)


app_name = "authentication"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("logout/", CustomUserLogoutView.as_view(), name="user-detail"),
    path(
        "registration/",
        CustomUserRegistrationView.as_view(),
        name="registration",
    ),
    path("user/<pk>/", CustomUserDetailView.as_view(), name="user-detail"),
]
