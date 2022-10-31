from product.forms import ProductForm
from product.models import Product
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError

# Guarda el modelo y define cuantos se mostraran en la lista


class ProductListView(ListView):
    model = Product
    paginate_by = 4

# Crear un nuevo Producto
class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('product:product-list')

    form_class = ProductForm

    def form_valid(self, form):
        data = form.cleaned_data
        actual_objects = Product.objects.filter(
            code_product=data['code_product'],
            name_product=data['name_product'],
            descrption_product=data['description_product'],
            existence=data['existence'],
            brand=data['brand']
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f'El producto {data['code_product'] - data['name_product']} ya está creado',
            )
            form.add_error('name', ValidationError('Accion no válida'))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f'El producto {data['code_product'] - data['name_product']} se creo exitosamente!',
            )
            return super().form_valid(form)
