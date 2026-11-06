from django.shortcuts import render,redirect
from Employee_Management_App.models import Employee
from Employee_Management_App.form import forms, EmployeeForm, RegisterForm
from Employee_Management_App.form1 import forms,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import secrets

@ login_required(login_url='/')
def employee_list_view(request):
    employee_list=Employee.objects.all()
    context={
        'employee_list':employee_list
    }
    return render(request,'employee_list.html',context)

@login_required(login_url='/')
def create_employee_view(request):
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list_view')
        else:
            context={
                'form':form
            }
            return render(request,'create_list.html',context)
    else:
        form=EmployeeForm()
        context={
            'form':form
        }
        return render(request,'create_list.html',context)
def employee_detail_view(request,pk):
    try:
        employee=Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        context={
            'message':f'Employee {pk} Does Not Exist'
        }
        return render(request,'employee_detail.html',context)
    else:
        context={
            'employee':employee
        }
        return render(request,'employee_detail.html',context)
def employee_update_view(request,pk):
    try:
        employee=Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        context={
            'message':f'Employee {pk} Does Not Exist'
        }
        return render(request,'employee_update.html',context)
    if request.method == 'POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list_view')
        else:
            context={
                'form':form,
                'employee':employee
            }
            return render(request,'employee_update.html',context)
    else:
        form=EmployeeForm(instance=employee)
        context={
            'form':form,
            'employee':employee
        }
        return render(request,'employee_update.html',context)
def employee_delete_view(request,pk):
    global employee
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list_view')
    try:
        employee=Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        context={
            'message':f'Employee {pk} Does Not Exist'
        }
        return render(request,'employee_delete.html',context)
    else:
        context={
            'employee':employee
        }
        return render(request,'employee_delete.html',context)
def login_view(request):

    if request.method == 'POST':

        form1 = LoginForm(request.POST)

        if form1.is_valid():

            username = form1.cleaned_data['username']
            password = form1.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)

                next_url = request.GET.get('next')

                if next_url:
                    return redirect(next_url)

                return redirect('employee_list_view')

    else:
        form1 = LoginForm()
        context = {
            'form1': form1
        }

        return render(request, 'login.html', context)
def logout_view(request):
    logout(request)
    return redirect('login')



def register_view(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f'Account {username} created successfully!')
            return redirect('/')
        else:
            username=request.POST.get('username')
            messages.warning(request,f'Account {username} Not Created')
    else:
        form=RegisterForm()
        context={
            'form':form
        }
        return render(request,'register.html',context)

def about_view(request):
    return render(request,'about.html')
