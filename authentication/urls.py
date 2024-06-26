from django.urls import path
from .views import user_login, user_logout, UserRegisterView, forgot_password, ResetPasswordView

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset_password'),
]
