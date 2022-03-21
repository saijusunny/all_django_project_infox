from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup_details/', views.signup_details, name='signup_details'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name="home"),
    path('edit_details/<int:pk>', views.edit_details, name='edit_details'),
    path('complete_pro/', views.complete_pro, name='complete_pro'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    path('delete_items/<int:pk>', views.delete_items, name='delete_items'),
    path('edit_details/<int:pk>', views.edit_details, name='edit_details'),
    

    #admin Section------------------------------------------------------------
    path('upload_product/', views.upload_product, name='upload_product'),
    path('add_product/', views.add_product, name='add_product'),
     path('addproduct_page/',views.addproduct_page,name='addproduct_page'),
    path('ourpro/',views.ourpro,name='ourpro'),
     #------------------------------------------------------------------------


     # user product view sections---------------------------------
     path('pro_home/', views.pro_home, name='pro_home'),
     path('shop/<int:pk>', views.shop, name='shop'),
     path('shop2/<int:pk>', views.shop2, name='shop2'),
     path('cart/<int:pk>', views.cart, name='cart'),
     path('add_curt',views.add_curt, name='add_curt'),
     path('curt_view/', views.curt_view, name='curt_view'),
     path('delete_cart/<int:pk>', views.delete_cart, name='delete_cart'),
    #-------------------------------------------------------------------------
   


    #login Section
    path('usercreate/', views.usercreate, name='usercreate'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),

]