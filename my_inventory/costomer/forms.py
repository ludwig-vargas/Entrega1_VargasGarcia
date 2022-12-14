from django import forms
from costomer.models import Costomer

class CostomerForm(forms.ModelForm):
    code_cost = forms.CharField(
        label='Codigo del cliente',
        required=False,
        widget=forms.TextInput(
          attrs={
                'class': 'cost-code',
                'placeholder': 'Codigo del cliente',
                'required': 'True',
                'type':'text',
                'minlength':'3',
                'maxlength':'3',
          }  
        ),
    )
    name_cost = forms.CharField(
        label='Nombre del cliente',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'cost-name',
                'placeholder': 'Nombre del empleado',
                'required': 'True',
            }
        ),
    )
    last_name_cost = forms.CharField(
        label='Apellido del cliente',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'cost-last-name',
                'placeholder': 'Apellido del cliente',
                'required': 'True',
            }
        ),
    )
    phone_number_cost = forms.IntegerField(
        label='Numero de telefono',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'cost-phone-number',
                'placeholder': 'Numero de telefono',
                'required': 'True',
                'type':'number',
            }
        ),
    )
    
    class Meta:
        model = Costomer
        fields = ["code_cost", "name_cost", "last_name_cost", "phone_number_cost"]
