from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('productmen/',product, name='product'),
    path('men/',men, name='men'),
    path('women/',women, name='women'),
    path('girl/',girl, name='girl'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),

    #============== registration form ===========

    path('registerdata/',registerdata, name='registerdata'),
    path('signup/',signup, name='signup'),

    # ============== login =================================

    path('logindata/',logindata, name='logindata'),
    path('logout/',logout, name='logout'),
    path('editpro/',editpro, name='editpro'),
    path('updatepro_img/',updatepro_img, name='updatepro_img'),
    path('userprofile/', userprofile, name='userprofile'),
    path('forgetpass/',forgetpass, name='forgetpass'),
    path('setfogetpass1/',setfogetpass1, name='setfogetpass1'),
    path('otpforgpass/',otpforgpass, name='otpforgpass'),
    path('changepass/', changepass, name='changepass'),
    path('passwordchange/', passwordchange, name='passwordchange'),
    path('setforget_password/', setforget_password, name='setforget_password'),

    # ============= add To Cart Page ======================================
    path('addtocart/<int:pk>',addtocart, name='addtocart'),
    path('decrement/',decrement, name='decrement'),
    path('increment/',increment, name='increment'),
    path('removeadd_cart/<int:pk>/',removeadd_cart, name='removeadd_cart'),
    path('cartpage/', cartpage, name='cartpage'),

    # ===================== Payment Checkout Url ==============================
    path('checkout/', checkout, name='checkout'),
    path('making_payment/', making_payment, name='making_payment'),
    path('invoice_load/<str:pk>/', invoice_load, name='invoice_load'),
    path('buyproduct/', buyproduct, name='buyproduct'),
    path('buyproduct_payment/', buyproduct_payment, name='buyproduct_payment'),


    # ============= userdashboard =========================================
    path('customerquery', customerquery, name='customerquery'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)