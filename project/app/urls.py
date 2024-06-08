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
    path('buyproduct/', buyproduct, name='buyproduct'),
    path('buyproduct_payment/', buyproduct_payment, name='buyproduct_payment'),


    # ============= userdashboard =========================================
    path('customerquery', customerquery, name='customerquery'),













    # ============= Admin Dashboard =====================
    path('Adminlogout/',Adminlogout, name='Adminlogout'),
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

    # =============== Registration data CRUD ===================
    path('editregistdata/<int:pk>/',editregistdata, name='editregistdata'),
    path('deletregistdata/<int:pk>/',deletregistdata, name='deletregistdata'),
    path('updateeditregistdata/',updateeditregistdata, name='updateeditregistdata'),

    # =============== Product data CRUD ===============================================
    path('editproductdata/<int:pk>/',editproductdata, name='editproductdata'),
    path('deletproductdata/<int:pk>/',deletproductdata, name='deletproductdata'),
    path('updateditproductdata/',updateditproductdata, name='updateditproductdata'),
    path('addproductdata/',addproductdata, name='addproductdata'),




    # path('update_cart_quantity/<int:pk>/<str:action>/', update_cart_quantity, name='update_cart_quantity'),

    



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)