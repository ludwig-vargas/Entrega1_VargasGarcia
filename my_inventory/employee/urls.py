from django.urls import path
from employee import views

app_name = 'employee'
urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/add/', views.EmployeeCreateView.as_view(), name='employee-add'),
]