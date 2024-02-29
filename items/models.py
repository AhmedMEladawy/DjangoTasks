from django.db import models

# Create your models here.
    

class Products(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    price = models.DecimalField( max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='items/images/%y/%m/%d', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
