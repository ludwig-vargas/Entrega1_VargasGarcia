from costomer.forms import CostomerForm
from costomer.models import Costomer
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.
# Guarda el modelo y define cuantos se mostraran en la lista
class CostomerListView(ListView):
    model = Costomer
    paginate_by = 4

# Crear un nuevo Empleado
class CostomerCreateView(CreateView):
    model = Costomer
    success_url = reverse_lazy("costomer:costomer-list")

    form_class = CostomerForm
 
    def form_valid(self, form):
        """Filter to avoid duplicate courses"""
        data = form.cleaned_data
        actual_objects = Costomer.objects.filter(
            code_cost=data['code_cost'],
            name_cost=data['name_cost'],
            last_name_cost=data['last_name_cost'],
            phone_number_cost=data['phone_number_cost'],
            email_cost=data['email_cost']
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El cliente {data['name_cost']} {data['last_name_cost']} - {data['code_cost']} ya esta creado",
            )
            form.add_error('name', ValidationError('Acción no válida'))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"El cliente  {data['name_cost']} {data['last_name_cost']} - {data['code_cost']} se creo exitosamente!"
            )
            return super().form_valid(form)