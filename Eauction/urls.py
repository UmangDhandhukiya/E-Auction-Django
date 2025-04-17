from django.contrib import admin
from django.urls import path
from Eauction import views

urlpatterns = [
    path('', views.reg, name='reg'),
    path('login/', views.loginpage, name='loginpage'),
    path('base/', views.index, name='home'),
    path('logout/', views.logoutpage, name='logout'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('final/<str:pk>/', views.final, name='final'),
    path('bidpage/', views.bidpage, name='bidpage'),
    # path('showall/', views.showall, name='showall'),  # Optional
]
