from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('batch/', views.batch, name='batch'),
    path('batch/batchrecord/', views.batchrecord, name='batchrecord'),
    path('inventory/', views.inventory, name='inventory'),

    


]