from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    data_typed_items = models.TextField()
    email = models.EmailField()
    github_link = models.URLField(null=True, blank=True)
    linkedin_Link = models.URLField(null=True, blank=True)

class AboutSection(models.Model):
    name = models.ForeignKey('BasicInfo', on_delete=models.CASCADE)
    about_description = models.TextField()
    birthday = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(max_length=100)
    degree = models.CharField(max_length=200)

class SkillLevel(models.Model):
    name = models.ForeignKey('BasicInfo', on_delete=models.CASCADE)
    HTMLSkillLevel = models.IntegerField(max_length=100)
    CSSSkillLevel = models.IntegerField(max_length=100)
    JSSkillLevel = models.IntegerField(max_length=100)
    PythonSkillLevel = models.IntegerField(max_length=100)
    PhotoshopSkillLevel = models.IntegerField(max_length=100)

class ContactUs(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField()



def __str__(self):
    return self.title
