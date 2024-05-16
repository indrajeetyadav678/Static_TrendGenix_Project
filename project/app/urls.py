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
    path('logout/',logout, name='logout'),
    path('editpro/',editpro, name='editpro'),
    # ============= dashboard page =============
    path('todotask/',todotask, name='todotask'),
    # path('search/',search, name='search'),
    path('showdata1/<str:pk>/',showdata1, name='showdata1'),
    path('showdata2/',showdata2, name='showdata2'),

]