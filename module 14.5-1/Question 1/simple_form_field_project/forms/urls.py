from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'register'),
    path('contact/',views.contact,name = 'contact')
]
