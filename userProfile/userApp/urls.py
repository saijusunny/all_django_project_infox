from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('load_profile_page',views.load_profile_page,name='load_profile_page'),
    path('add_profile',views.add_profile,name='add_profile'),
    path('show_details',views.show_details,name='show_details'),
    path('edit_user_page/<int:pk>',views.edit_user_page,name='edit_user_page'),
    path('edit_user_data/<int:pk>',views.edit_user_data,name='edit_user_data'),
    path('delete_user_data/<int:pk>',views.delete_user_data,name='delete_user_data'),

    #....Add Multiple Image...
    path('pro_home',views.pro_home,name='pro_home'),
    path('addproduct_page',views.addproduct_page,name='addproduct_page'),
    path('add_product',views.add_product,name='add_product'),
    #path('addimage_page',views.addimage_page,name='addimage_page'),
    path('add_image/<int:pk>',views.add_image,name='add_image'),
    path('product_details/<int:pk>',views.product_details,name='product_details'),

    #.....Gallery.....
    path('addimage',views.addimage,name='addimage'),
    path('add',views.add,name='add'),
    path('gallery',views.gallery,name='gallery'),
    path('showimage/<int:pk>',views.showimage,name='showimage'),
    
]