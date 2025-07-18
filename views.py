from django.shortcuts import render, redirect
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        email = request.POST['email']
        salary = request.POST['salary']
        Employee.objects.create(name=name, department=department, email=email, salary=salary)
        return redirect('employee_list')
    return render(request, 'employee/add.html')
