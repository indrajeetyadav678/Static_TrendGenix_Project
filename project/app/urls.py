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
    path('showdata2/',showdata2, name='showdata2'),
    path('edittodo/<int:pk>/',edittodo, name='edittodo'),
    path('delettodo/<int:pk>/',delettodo, name='delettodo'),
    path('updatedata/',updatedata, name='updatedata'),

]