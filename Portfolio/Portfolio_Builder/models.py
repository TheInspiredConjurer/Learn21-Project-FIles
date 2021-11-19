from django.db import models

# Create your models here.

class Person(models.Model):
    Full_Name = models.CharField("person's first name", max_length=250)
    Email = models.EmailField("person's email", max_length=254)
    Phone_Number = models.IntegerField("person's phone number")
    Location = models.CharField("person's short address", max_length=100)
    Github_Link = models.CharField("person's github link", max_length=250)

    
    
