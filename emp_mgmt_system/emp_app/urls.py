from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("view_all_employees",views.view_all_employees,name="index"),

    path("add_new_employee",views.add_new_employee,name="index"),
    path("view_employee_form",views.view_employee_form,name="index"),

    path("remove_employee",views.remove_employee,name="index"),
    path("all_employees_to_remove",views.all_employees_to_remove,name="index"),
    
    path("filter_employee",views.filter_employee,name="index"),
    path("download_csv_file",views.download_csv_file,name="index")
    
]
