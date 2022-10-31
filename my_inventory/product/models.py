from django.db import models

# Create your models here.
class Product(models.Model):
    code_product = models.CharField(primary_key = True, max_length = 3)
    name_product = models.CharField(max_length = 40)
    description_product = models.CharField(max_length = 50)
    existence = models.IntegerField()
    brand = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'Code: {self.code_product} | Name product: {self.name_product} | Brand: {self.brand} | Existence: {self.existence}'