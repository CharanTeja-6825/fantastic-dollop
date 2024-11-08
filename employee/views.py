from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

#=========================================Employee Dashboard View=====================================================#

def employee_dashboard(request):
    return render(request, 'employee/employee_homepage.html')

def employee_list(request):
    # Filter users with 10-digit usernames (assuming this signifies employees)
    employees = User.objects.filter(username__regex=r'^\d{10}$')
    return render(request, 'employee/employee_details.html', {'employees': employees})

def delete_employee(request, user_id):
    # Retrieve the user by ID
    employee = get_object_or_404(User, id=user_id, username__regex=r'^\d{10}$')
    # Delete the employee
    employee.delete()
    messages.success(request, "Employee deleted successfully.")
    # Redirect to the employee list page
    return redirect('employee_list')

#=====================================================================================================================#
