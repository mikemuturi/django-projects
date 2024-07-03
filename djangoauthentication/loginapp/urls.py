from django.urls import path
from loginapp import views

urlpatterns = [
    path('', views.index, name='index'),  # Corrected path
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
