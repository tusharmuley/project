from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import employee, department, role
from datetime import datetime

from django.db.models import Q
import csv
import openpyxl



# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_all_employees(request):
    all_emp=employee.objects.all()
    context={
        "all_emp":all_emp,
    }
    # print(context)
    return render(request, 'view_all_employees.html',context)

def add_new_employee(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        dept=int(request.POST['dept'])
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        phone=request.POST['phone']
        role_id=int(request.POST['role'])
        
        dept=department.objects.get(id=dept)
        role_data=role.objects.get(id=role_id)
        # all_emp=department.objects.all()
        # print("log",all_emp[0].id)
        # return HttpResponse()
        emp=employee(firstname=firstname, lastname=lastname, salary=salary, bonus=bonus, phone=phone, dept=dept, role=role_data, hire_date=datetime.now())
        emp.save()
        
        
        return HttpResponse("employee added successfully")
    # if request.method == 'GET':
        # return render(request, 'add_new_employee.html')
        
    else:
        return JsonResponse("SOMETHING WENT WRONG")
    

def view_employee_form(request):
    all_dept=department.objects.all()
    all_role=role.objects.all()
    
    context={
        "all_dept":all_dept,
        "all_role":all_role
    }
    # print(context)
    return render(request, 'add_new_employee.html',context)


def remove_employee(request):
    if request.method=="POST":
        emp_id=request.POST["id"]
        obj=employee.objects.get(id=emp_id)
        obj.delete()
        return HttpResponse(obj.firstname+" "+obj.lastname+" employee is deleted successfully")
    elif request.method=="Get":
        return render(request, 'remove_employee.html')
    else:
        return HttpResponse("Something went wrong")

def all_employees_to_remove(request):
    all_emp=employee.objects.all()
    context={
        "all_emp":all_emp
    }
    return render(request, 'remove_employee.html',context)



def filter_employee(request):
    if request.method=="POST":
        name=request.POST["name"]
        dept=request.POST["dept"]
        role=request.POST["role"]
        all_emp_data=employee.objects.all()
        if name:
            all_emp=all_emp_data.filter(Q(firstname__icontains=name) | Q(lastname__icontains=name))
        if dept:
            all_emp=all_emp_data.filter(dept__name__icontains=dept)
        if role:
            all_emp=all_emp_data.filter(role__name__icontains=role)

        context={
            "all_emp":all_emp,
        }

        return render(request, 'view_all_employees.html',context)
    else:
        return render(request, "filter_employee.html")


def download_csv_file(request):
        # Data to write to file
        datas=employee.objects.all()
        data=[]
        import openpyxl

        # Load the Excel workbook
        workbook = openpyxl.Workbook()

        # Select the worksheet
        worksheet = workbook.active

        # Define the headers for your data
        headers = ['id', 'firstname', 'lastname',"Department","sallary","bonus", "role","phone","hire_date"]

        # Write the headers to the first row of the worksheet
        worksheet.append(headers)

        # Loop through the Django objects and write the data to the worksheet
        for obj in datas:
            data = [obj.id, obj.firstname,obj.lastname, obj.dept.name, obj.salary, obj.bonus, obj.role.name, obj.phone,obj.hire_date]
            worksheet.append(data)

        # Save the changes to the Excel workbook
        workbook.save('C:/Users/Administrator/Desktop/projects/temp_files/example.xlsx')
        # for d in datas:
        #     all_emp={
        #         "id":d.id,
        #         "firstname":d.firstname,
        #         "lastname":d.lastname,
        #         "dept":d.dept.name,
        #         "salary":d.salary,
        #         "bonus":d.bonus,
        #         "role":d.role.name,
        #         "phone":d.phone,
        #         "hire_data":d.hire_date
        #     }
        #     data.append(all_emp[1])
        return HttpResponse("excel sheet downloaded")
        
        

