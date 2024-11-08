from django.urls import path
from . import views

urlpatterns = [
    path('employee_homepage/', views.employee_dashboard, name='employee_homepage'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/delete/<int:user_id>/', views.delete_employee, name='delete_employee'),
]
