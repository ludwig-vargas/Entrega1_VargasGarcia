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