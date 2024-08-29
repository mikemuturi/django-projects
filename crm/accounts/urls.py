from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user-page/', views.userPage, name='user-page'),

    path('account/', views.accountSettings, name='account'),

    path('customer/<int:pk>/', views.customer, name='customer'),
    path('products/', views.products, name='products'),
    path('create_order/<int:pk>/', views.create_order, name='create_order'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('about/', views.about, name='about'),
]
