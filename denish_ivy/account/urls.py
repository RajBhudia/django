from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from account.views import MyView, HomePageView
from .views import HomePageView , CustomerView
from django.views.generic.base import RedirectView
from account.views import ProductView


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
   # path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>,<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name= "password_reset_complete"),


    path('mine/', MyView.as_view(), name='my-view'),
    path ('product/', HomePageView.as_view(template_name = "products.html"), name='product'),
    
    path('about/', MyView.as_view()),
    
    path('c_custom/<str:pk_test>/', views.Customer1View.as_view(template_name='account/customer.html'), name='customer'),



    path('c_product/', views.ProductView.as_view(), name='product'),
    path('c_dashboard/', views.DashboardView.as_view(), name='dashbaord'),
    path('c_customer/<str:pk_test>/', views.CustomerView.as_view(), name='customer'),
    path('c_create_order/<str:pk>/', views.CreateOrderView.as_view(), name='create order'),
    path('c_register/', views.RegisterView.as_view(), name='register'),
    path('c_update_order/<str:pk>/', views.UpdateOrderView.as_view(), name='update_order'),
    path('c_delet_order/<str:pk>/',views.DeletOrderView.as_view(), name='delet_order'),



    path('ad/', views.HomeTemplateView.as_view(template_name='account/dashboard.html'), name='home'),
  


]    