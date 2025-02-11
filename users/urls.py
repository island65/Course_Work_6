from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, ProfileView, reset_password, UserLoginView, logout

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path('logout/', logout, name='logout'),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("reset_password/", reset_password, name="reset_password"),
]