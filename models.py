from django.db import models

# Create your models here.
class Appoint_Consultant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    appointment = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
class Get_in_touch(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    comment=models.TextField()

    def __str__(self):
        return self.name
    
