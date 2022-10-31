from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    code_emp = forms.CharField(
        label='Codigo del empleado',
        required=False,
        widget=forms.TextInput(
          attrs={
                'class': 'employee-code',
                'placeholder': 'Codigo del empleado',
                'required': 'True',
                'type':'text',
                'minlength':'3',
                'maxlength':'3',
          }  
        ),
    )
    name_emp = forms.CharField(
        label='Nombre del empleado',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'employee-name',
                'placeholder': 'Nombre del empleado',
                'required': 'True',
            }
        ),
    )
    last_name_emp = forms.CharField(
        label='Apellido del empleado',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'employee-last-name',
                'placeholder': 'Apellido del empleado',
                'required': 'True',
            }
        ),
    )
    job_emp = forms.CharField(
        label='Puesto de trabajo',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'employee-job',
                'placeholder': 'Puesto de trabajo',
                'required': 'True',
            }
        ),
    )
    work_area_emp = forms.CharField(
        label='Area de trabajo',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'employee-work-area',
                'placeholder': 'Area de trabajo',
                'required': 'True',
            }
        ),
    )
    
    class Meta:
        model = Employee
        fields = ["code_emp", "name_emp", "last_name_emp","job_emp","work_area_emp"]