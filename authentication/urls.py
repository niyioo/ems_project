from django.urls import path
from .views import user_login, user_logout, UserRegisterView

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
]
