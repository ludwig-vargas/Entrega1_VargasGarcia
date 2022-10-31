from employee.forms import EmployeeForm
from employee.models import Employee
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.
# Guarda el modelo y define cuantos se mostraran en la lista
class EmployeeListView(ListView):
    model = Employee
    paginate_by = 4

# Crear un nuevo Empleado
class EmployeeCreateView(CreateView):
    model = Employee
    success_url = reverse_lazy("employee:employee-list")

    form_class = EmployeeForm

    def form_valid(self, form):
        """Filter to avoid duplicate courses"""
        data = form.cleaned_data
        actual_objects = Employee.objects.filter(
            code_emp=data['code_emp'],
            name_emp=data['name_emp'],
            last_name_emp=data['last_name_emp'],
            job_emp=data['job_emp'],
            work_area_emp=data['work_area_emp']
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El empleado {data['name_emp']} {data['last_name_emp']} - {data['code_emp']} ya esta creado",
            )
            form.add_error('name', ValidationError('Acción no válida'))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"El empleado {data['name_emp']} {data['last_name_emp']} - {data['code_emp']} se creo exitosamente!"
            )
            return super().form_valid(form)