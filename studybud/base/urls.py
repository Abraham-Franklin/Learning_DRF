from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.retrieve_task, name="task-list"),
    path('tasks/<int:pk>/', views.task_details, name="task_detail"),
]