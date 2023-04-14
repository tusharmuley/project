import json
from django.shortcuts import render
from django.http import JsonResponse
from emp_app.models import employee, department, role
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

@csrf_exempt
def all_emplyees(request):
    if request.method=="POST":
        user_id=request.POST['id']
        try:
            data=employee.objects.get(id=int(user_id))
        except employee.DoesNotExist:
            return JsonResponse({"status":"fail","message":"user not found with this id"})

        json_data={
            "id":data.id,
            "firstname":data.firstname,
            "lastname":data.lastname,
            "dept":data.dept.name,
            "salary":data.salary,
            "bonus":data.bonus,
            "role":data.role.name,
            "phone":data.phone,
            "hire_data":data.hire_date

        }

        return JsonResponse({"status":"success","message":"user fetched successfully","user_details":json_data})
    
    if request.method=="GET":
        emp_data=employee.objects.all()
        emp_data_list=[]
        for i in emp_data:
            emp_data_list.append({"id":i.id,"firstname":i.firstname,"lastname":i.lastname, "department":str(i.dept), "salary":i.salary})
        print(emp_data_list)
        return JsonResponse({"status":"success","message":"all employees fected successfully","all_employees":emp_data_list})
        # return JsonResponse({"status":"success","message":"all employees fected successfully","all_employees":emp_data_list})
        
    else:
        return JsonResponse({"status":"fail","message":"method not found"})

@csrf_exempt
def add_new_employee(request):
    if request.method=="POST":
        now=datetime.now()
        json_data = json.loads(request.body)
        # id = json_data['id']
        firstname = json_data['firstname']
        lastname = json_data['lastname']
        dept = json_data["dept_id"]
        salary = json_data["salary"]
        bonus = json_data["bonus"]
        role = json_data["role_id"]
        phone = json_data["phone"]
        # hire_date = models.DateField()
        try:
            obj=employee()
            obj.firstname=firstname
            obj.lastname=lastname
            obj.dept_id=dept
            obj.salary=salary
            obj.bonus=bonus
            obj.role_id=role
            obj.phone=phone
            obj.hire_date=now
            obj.save()
        except Exception as e:
            return JsonResponse({"status":"fail","message":"something went wrong in adding employee. error is :"+str(e),"status_code":405})
        
        return JsonResponse({"status":"success","message":"employee added successfully","status_code":200})

    else:
        return JsonResponse({"status":"fail","message":"method not found","status_code":405})
    


@csrf_exempt
def all_departments_fn(request):
    if request.method=="POST":
        all_dept=department.objects.all()
        all_dept_data=[]
        for i in all_dept:
            all_dept_data.append({"id":i.id,"name":i.name, "location":i.location})

        return JsonResponse({"status":"success","message":"fetched successfully","all_departments":all_dept_data,"status_code":200})

    else:
        return JsonResponse({"status":"fail","message":"method not found","status_code":405})

