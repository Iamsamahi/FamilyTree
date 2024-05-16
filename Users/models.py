from django.db import models

# Create your models here.
class Person(models.Model):
    user_name = models.CharField(max_length=125, unique=True ,primary_key=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(null=True)
    dob = models.DateField(null=True , blank=True)
    gender = models.CharField(max_length=10)
    password1 = models.CharField(max_length=20)
    password2= models.CharField(max_length=20)
    

    def __str__(self):
        return self.user_name+": " + self.first_name +" "+self.last_name 
    
     