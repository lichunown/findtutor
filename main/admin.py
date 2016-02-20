from django.contrib import admin

# Register your models here.
from .models import Student,Tutor,Project

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Project)