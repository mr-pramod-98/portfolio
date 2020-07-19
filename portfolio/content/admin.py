from django.contrib import admin
from .models import Certifications, GroupProjects, PersonalProjects

# Register your models here.
admin.site.register(Certifications)
admin.site.register(GroupProjects)
admin.site.register(PersonalProjects)
