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

    # ============== login =================================

    path('logindata/',logindata, name='logindata'),
    path('logout/',logout, name='logout'),
    path('editpro/',editpro, name='editpro'),
    path('forgetpass/',forgetpass, name='forgetpass'),
    path('changepass/', changepass, name='changepass'),
    path('passwordchange/', passwordchange, name='passwordchange'),

    # ============= userdashboard =======================
    # ============= Admin Dashboard =====================

    path('dashbordindex/',dashbordindex, name='dashbordindex'),
    path('productdata/',productdata, name='productdata'),
    path('userdata/',userdata, name='userdata'),
    path('result/',result, name='result'),
    path('product_entry/',product_entry, name='product_entry'),

    # ============= cruid dashboard page =============

    path('todoform/',todoform, name='todoform'),
    path('todotask/',todotask, name='todotask'),
    path('showdata2/',showdata2, name='showdata2'),
    path('edittodo/<int:pk>/',edittodo, name='edittodo'),
    path('delettodo/<int:pk>/',delettodo, name='delettodo'),
    path('updatedata/',updatedata, name='updatedata'),

    # ========== product data save Show ============

    path('product_show1/',product_show1, name='product_show1'),
    path('addtocart/<int:pk>',addtocart, name='addtocart'),
    path('cartpage/', cartpage, name='cartpage'),
    # path('update_cart_quantity/<int:pk>/<str:action>/', update_cart_quantity, name='update_cart_quantity'),

    # ===================== Payment Checkout Url ==============================
    path('checkout/', checkout, name='checkout'),
    path('making_payment/', making_payment, name='making_payment'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)