from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
#    path('add', views.add, name="add"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('complete/<int:id>', views.complete, name="complete"),
    ]