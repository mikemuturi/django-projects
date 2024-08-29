from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Assuming you have a blog app with a home view
    path('users/', include('users.urls')),
]
