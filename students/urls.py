from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lecture/', views.lecture, name='lecture'),
    path('tasks/', views.tasks, name='tasks'),
]
