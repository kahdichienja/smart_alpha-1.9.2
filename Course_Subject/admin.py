from django.contrib import admin
from . models import Subject, SubjectSyllabus, SubjectObjective
# Register your models here.

admin.site.register(Subject)
admin.site.register(SubjectSyllabus)
admin.site.register(SubjectObjective)