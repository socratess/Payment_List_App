from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib import admin

# Create your models here.

class Bill(models.Model):
    title = models.CharField(max_length=200,validators=[MinLengthValidator(2,"The title of the bill needs to be at least 2 characters")])
    description = models.TextField(validators=[MinLengthValidator(2,"The description of the bill needs to be at least 2 characters")])
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.title+' --- '+str(self.price)
    
    def natural_key(self):
        return (self.title)
    
    
class BankEntity(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(
        2, "The name of the bank entity needs to be at least 2 characters")])
    frequent = models.BooleanField(default=False)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    
    def natural_key(self):
       return (self.name)
    
    def __str__(self):
        return self.name
