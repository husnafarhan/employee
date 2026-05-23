from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm



# Add Employee
def add_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/view/')

    else:
        form = EmployeeForm()

    return render(request, 'addemployee.html', {'form': form})


# View All Employees
def view_employees(request):

    employees = Employee.objects.all()

    return render(request, 'viewemployees.html', {'employees': employees})


# View Single Employee
def single_employee(request, id):

    employee = Employee.objects.get(id=id)

    return render(request, 'singleemployee.html', {'employee': employee})


# Update Employee
def update_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':

        form = EmployeeForm(request.POST,
                            request.FILES,
                            instance=employee)

        if form.is_valid():
            form.save()
            return redirect('/view/')

    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'updateemployee.html', {'form': form})


# Delete Employee
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('/view/')