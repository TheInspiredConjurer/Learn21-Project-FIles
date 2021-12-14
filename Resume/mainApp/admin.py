from django.contrib import admin

# Register your models here.

from .models import BasicInfo, AboutSection, SkillLevel, ContactUs

admin.site.register(BasicInfo)
admin.site.register(AboutSection)
admin.site.register(SkillLevel)
admin.site.register(ContactUs)