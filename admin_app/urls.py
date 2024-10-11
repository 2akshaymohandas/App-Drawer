from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [

    path('Apps-details', views.Apps_details, name="Apps_details"),
]