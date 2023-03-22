from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import Employee
# from django.db.models import Q
#  username and password for django admin
# username= Employeepassword= 3214

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)  

    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        role = request.POST.get('role')
        phone = int(request.POST.get('phone'))
        # hire =int( request.POST['hire'])
        add_emp = Employee(first_name=first_name, last_name=last_name, dept=dept,
                           salary=salary, bonus=bonus, role=role, phone=phone, hire_date=datetime.now())
        add_emp.save()

        messages.success(request, 'your message has been submitted!')
        return render(request, 'add_emp.html')
       
  

    return render(request, 'add_emp.html')


def remove_emp(request, emp_id=0):
    
    if emp_id:
        try:
            emp_to_be_removed= Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully!')
        except:
            return HttpResponse('please enter a valid emp_id')    

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'remove_emp.html', context)

def filter_emp(request):

    if request.method == 'POST' :
        first_name = request.POST['first_name']
      
        emps=Employee.objects.all()
        if first_name:
            emps=emps.filter(first_name__icontains=first_name)
             
            context={
                'emps':emps
            }
            return render(request,'all_emp.html',context )
    elif request.method=='GET':
        return render(request,'filter_emp.html' ) 
    else:
        return HttpResponse('an exception occured!')

    # return render(request,'filter_emp.html')


