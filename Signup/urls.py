from django.urls import path
from . import views

urlpatterns = [
    path('', views.empSignup, name='empSignup'),
    path('signin/', views.empSigninAction, name='empSigninAction'),
    path('dealerSignup/', views.dealerSignup, name='dealerSignup'),
    path('dealerSignup/dealerSigninAction/', views.dealerSigninAction, name='dealerSigninAction'),
    path('customerSignup/', views.customerSignup, name='customerSignup'),
    path('customerSignup/customerSignupAction/', views.customerSignupAction, name='customerSignupAction'),

]