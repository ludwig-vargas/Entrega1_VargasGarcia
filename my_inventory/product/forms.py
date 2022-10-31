from django import forms
from product.models import Product

class ProductForm(forms.ModelForm):
    code_product = forms.CharField(
        label='Codigo del producto',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'product-code',
                'placeholder': 'codigo del producto',
                'required': 'True',
                'type':'text',
                'minlength':'3',
                'maxlength':'3',
            }
        ),
    )
    name_product = forms.CharField(
        label='Nombre del producto',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'product-name',
                'placeholder': 'Nombre del producto',
                'required': 'True',
            }
        ),
    )
    description_product = forms.CharField(
        label='Descripcion del producto',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'product-description',
                'placeholder': 'Descripcion del producto',
                'required': 'True',
            }
        ),
    )
    existence = forms.IntegerField(
        label='Existencia del producto',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'product-existence',
                'placeholder': 'Existencia del producto',
                'required': 'True',
                'type':'number',
            }
        ),
    )
    brand = forms.CharField(
        label='Marca del producto',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'product-brand',
                'placeholder': 'Marca del producto',
                'required': 'True',
            }
        ),
    )
    
    class Meta:
        model = Product
        fields = ["code_product", "name_product", "description_product", "existence", "brand"]