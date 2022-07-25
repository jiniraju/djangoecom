from django.urls import path
from . import views

urlpatterns = [
    path('',views.load_home,name='load_home'),
    path('load_login/',views.load_login,name='load_login'),
    path('load_signup/',views.load_signup,name='load_signup'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('userprofileview/',views.userprofileview,name='userprofileview'),
    path('load_add_catogery/',views.load_add_catogery,name='load_add_catogery'),
    path('add_catogery/',views.add_catogery,name='add_catogery'),
    path('load_admin_home/',views.load_admin_home,name='load_admin_home'),
    path('userdetails/',views.userdetails,name='userdetails'),
    path('catogery_Details/',views.catogery_Details,name='catogery_Details'),
    path('load_add_product/',views.load_add_product,name='load_add_product'),
    path('add_product/',views.add_product,name='add_product'),
    path('del_user/<int:pk>',views.del_user,name='del_user'),
    path('ProductDetails/',views.ProductDetails,name='ProductDetails'),
    path('del_product/<int:pk>',views.del_product,name='del_product'),
    path('UserProductDetails/',views.UserProductDetails,name='UserProductDetails'),
    path('load_edit/',views.load_edit,name='load_edit'),
    path('edit_user/',views.edit_user,name='edit_user'),
    path('load_cart/',views.load_cart,name='load_cart'),
    path('add_caart/<int:pk>',views.add_caart,name='add_caart'),
    path('del_item_cart/<int:pk>',views.del_item_cart,name='del_item_cart'),
    path('edit_product_details/<int:pk>',views.edit_product_details,name='edit_product_details'),
    
    
]
