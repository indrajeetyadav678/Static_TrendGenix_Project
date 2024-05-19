from django.urls import path
from .views import*


urlpatterns=[
    path('',index, name='index'),
    # path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
   
    #============== registration form ===========
    path('registerdata/',registerdata, name='registerdata'),
    path('register/',register, name='register'),

    # ============== login =====================
    path('login/',login, name='login'),
    path('logindata/',logindata, name='logindata'),
    path('logout/',logout, name='logout'),
    path('editpro/',editpro, name='editpro'),
    path('forgetpass/',forgetpass, name='forgetpass'),


    # ============= userdashboard =============
    # path('home/',home1, name='home1'),
    # path('about1/',about1, name='about1'),
    # path('contact1/',contact1, name='contact1'),
    # path('register1/',register1, name='register1'),
    path('changepass/', changepass, name='changepass'),
    # ============= dashboard page =============
    path('todotask/',todotask, name='todotask'),
    # path('search/',search, name='search'),
    path('showdata2/',showdata2, name='showdata2'),
    path('edittodo/<int:pk>/',edittodo, name='edittodo'),
    path('delettodo/<int:pk>/',delettodo, name='delettodo'),
    path('updatedata/',updatedata, name='updatedata'),

]