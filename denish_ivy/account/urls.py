from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('customer/<int:pk>/', views.customer,  name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<int:pk>/', views.updateOrder, name="update_order"),
    path('delet_order/<int:pk>/', views.deletOrder, name="delet_order"),
   # path('customer_all/', views.customerMain, name="customer_all")
   
]
