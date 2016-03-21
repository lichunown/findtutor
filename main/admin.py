from django.contrib import admin

# Register your models here.
from .models import Student,Tutor,Project,Picture,Invitation

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Project)
admin.site.register(Invitation)
admin.site.register(Picture)