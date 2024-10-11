from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    

    path('', views.apiOverview, name="apiOverview"),
    path('task-list/', views.taskList, name="taskList"),
    path('create-task', views.createTask, name="createTask"),
    path('task-detail/<str:pk>/', views.task_detail, name="task_detail"),
    path('task-update/<str:pk>/', views.task_Update, name="task_Update"),
    path('task-delete/<str:pk>/', views.task_delete, name="task_delete"),
    

    


]