from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
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