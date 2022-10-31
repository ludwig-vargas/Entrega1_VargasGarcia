from django.db import models

# Create your models here.
class Costomer(models.Model):
    code_cost = models.CharField(primary_key = True, max_length = 3)
    name_cost = models.CharField(max_length = 40)
    last_name_cost = models.CharField(max_length = 40)
    phone_number_cost = models.IntegerField()
    
    def __str__(self):
        return f'Code: {self.code_cost} | Name: {self.name_cost} {self.last_name_cost} | Phone: {self.phone_number_cost}'