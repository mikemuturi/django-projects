from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),  # Root URL for projects list
    path('project/<str:pk>/', views.project, name='project'),  # URL for a single project
    path('create-project/', views.createProject, name='create-project'),  # URL for creating a project
    path('update-project/<str:pk>/', views.updateProject, name='update-project'), 
     path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
]
