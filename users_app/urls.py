from django.urls import path

from .views import CustomUserSignUpView, LoginView, VerifyEmailView, CheckEmailVerificationView

urlpatterns = [

    path('login/', LoginView.as_view(), name='user_login'),
    path('signup/', CustomUserSignUpView.as_view(), name='user_signup'),

    # Email verification endpoint
    path('api/verify-email/<uuid:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('check-email-verification/', CheckEmailVerificationView.as_view(), name='check_email_verification'),
]