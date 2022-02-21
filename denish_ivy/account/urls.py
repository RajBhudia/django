from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from account.views import MyView, HomePageView
from .views import HomePageView , CustomerView


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>,<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name= "password_reset_complete"),


    # path('mine/', MyView.as_view(), name='my-view'),
    path ('dashboard', HomePageView.as_view(template_name = "login.html"), name='home'),
    path('temp1/', CustomerView.as_view(template_name = "customer.html"), name='customer'),
    path('about/', MyView.as_view()),
]