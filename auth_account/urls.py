from django.urls import path
from .views import UserSignupView, UserLoginView, CustomPasswordResetView, UserPasswordResetView, SendPasswordResetEmailView, UserProfileView

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="user_signup"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='custom_password_reset'),
    path('send-password-Email/', SendPasswordResetEmailView.as_view(), name='send_password_reset_email'),
    # path('reset-password-Email/<uid>/<token>/', UserPasswordResetView.as_view(), name="reset-password")
    path('reset-password-Email/<str:uidb64>/<str:token>/', UserPasswordResetView.as_view(), name='password_reset_confirm'),
]