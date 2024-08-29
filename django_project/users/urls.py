from django.urls import path
# from . import views as user_views
from . import views 
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset/done', views.password_reset_done, name='password_reset_done'),
    path('password-reset-confirm', views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete', views.password_reset_complete, name='password_reset_complete'),

    # path('register/', user_views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)