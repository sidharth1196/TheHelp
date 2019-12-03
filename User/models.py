from django.db import models
from Home.models import Work
from django.contrib.auth.models import User

# Create your models here.

class Worker(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    phone = models.CharField(max_length=15)
    basic_charge = models.DecimalField(max_digits=6, decimal_places=2)
    work = models.ManyToManyField(Work)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    total_money = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
        
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length = 150)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
