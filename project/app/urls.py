from django.urls import path
from .views import*


urlpatterns=[
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('registerdata/',registerdata, name='registerdata'),
    path('logindata/',logindata, name='logindata'),
]