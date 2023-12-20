from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegister,name = 'register'),
    path('user_login/', views.UserLogin,name = 'login'),
    path('user_logout/', views.UserLogout,name = 'usrLogout'),
    path('user_profile/', views.profile,name = 'profile'),
]
