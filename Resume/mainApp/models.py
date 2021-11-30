from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    subject_line = models.CharField(max_length=200)
    message = models.TextField()