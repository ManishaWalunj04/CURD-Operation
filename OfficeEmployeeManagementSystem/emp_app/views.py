from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Employee
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Employee
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        emai_id = request.POST['email_id']
        phone_no = int(request.POST['phone_no'])
        address = request.POST['address']
        new_emp = Employee(first_name=first_name, last_name=last_name, email_id=emai_id, phone_no=phone_no,
                           address=address)

        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == "GET":
        return render(request, 'add_emp.html')

    else:
        return HttpResponse("Employee  Has Not Been Added")


def remove_emp(request, id=0):
    if id:
        try:
            emp_to_be_remove = Employee.objects.get(id=id)
            emp_to_be_remove.delete()
            # return HttpResponse('Employee Remove successfully')
            messages.success(request, 'Employee Remove successfully')


        except:
            messages.warning(request, 'Please Enter Valid Employee Id')
            # return HttpResponse('Please Enter Valid Employee Id')

    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }

    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('Employee Not Found')


def edit_emp_profile(request, id):
    emp_profile = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        data = json.loads(request.body)

        emp_profile.first_name = data.get('first_name', emp_profile.first_name)
        emp_profile.last_name = data.get('last_name', emp_profile.last_name)
        emp_profile.email_id = data.get('email_id', emp_profile.email_id)
        emp_profile.phone_no = data.get('phone_no', emp_profile.phone_no)
        emp_profile.address = data.get('address', emp_profile.address)

        emp_profile.save()

        return JsonResponse({'message': 'Employee profile updated successfully'})

    return render(request, 'edit.html', {'user_profile': emp_profile})





