from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('teachers/', views.teachers, name='teachers'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),  # Add trailing slash
    path('register/', views.register, name='register'), # Add trailing slash
    path('logout/', views.logout, name='logout'),
    path('get_subjects/', views.get_subjects, name='get_subjects'),
]
