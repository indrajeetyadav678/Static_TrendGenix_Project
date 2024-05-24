from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('product/',product, name='product'),
    path('men/',men, name='men'),
    path('women/',women, name='women'),
    path('girl/',girl, name='girl'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),

    #============== registration form ===========

    path('registerdata/',registerdata, name='registerdata'),

    # ============== login =================================

    path('logindata/',logindata, name='logindata'),
    path('logout/',logout, name='logout'),
    path('editpro/',editpro, name='editpro'),
    path('forgetpass/',forgetpass, name='forgetpass'),
    path('changepass/', changepass, name='changepass'),

    # ============= userdashboard ==========================

    path('home/',home, name='home'),
    path('about1/',about1, name='about1'),
    path('contact1/',contact1, name='contact1'),
    path('product1/',product1, name='product1'),
    path('men1/',men1, name='men1'),
    path('women1/',women1, name='women1'),
    path('girl1/',girl1, name='girl1'),

    # ============= Admin Dashboard =====================

    path('dashbordindex/',dashbordindex, name='dashbordindex'),
    path('productdata/',productdata, name='productdata'),
    path('userdata/',userdata, name='userdata'),
    path('result/',result, name='result'),

    # ============= cruid dashboard page =============
    
    path('todoform/',todoform, name='todoform'),
    path('todotask/',todotask, name='todotask'),
    path('showdata2/',showdata2, name='showdata2'),
    path('edittodo/<int:pk>/',edittodo, name='edittodo'),
    path('delettodo/<int:pk>/',delettodo, name='delettodo'),
    path('updatedata/',updatedata, name='updatedata'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)