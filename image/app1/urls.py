"""task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path
from.import views
#from django.conf.urls.static import static
#from unicodedata import name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/', views.view, name='view'),
    path('product_details', views.product_details, name='product_details'),
    path('', views.add, name='add'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    path('edit_details/<int:pk>', views.edit_details, name='edit_details'),

    
]
