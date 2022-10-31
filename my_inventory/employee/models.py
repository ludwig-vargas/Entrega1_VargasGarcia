from django.db import models

# Create your models here.
class Employee(models.Model):
    code_emp = models.CharField(primary_key = True, max_length = 3)
    name_emp = models.CharField(max_length = 40)
    last_name_emp = models.CharField(max_length = 40)
    job_emp = models.CharField(max_length = 40)
    work_area_emp = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'Code: {self.code_emp} | Name: {self.name_emp} {self.last_name_emp} | Job: {self.job_emp} | Work Area: {self.work_area_emp}'