from django.urls import path
from . import views

urlpatterns = [
    path('', views.custemer_Product, name='custemer_Product'),
]