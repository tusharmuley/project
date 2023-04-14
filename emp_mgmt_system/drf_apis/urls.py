from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("all_emplyees/",views.all_emplyees,name="all_emplyees"),
    path("add_new_employee/",views.add_new_employee,name="add_new_employee"),
    path("all_departments_fn/",views.all_departments_fn,name="all_departments_fn"),
    
    
]