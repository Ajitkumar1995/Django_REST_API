from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=65,null=True)
    email=models.CharField(max_length=65)
    phone=models.CharField(max_length=10)
    desc=models.TextField(max_length=200)
    date=models.DateField(null=True,blank=True)
    def __str__(self):
        return self.name

