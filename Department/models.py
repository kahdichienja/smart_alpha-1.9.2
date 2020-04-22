from django.db import models
from django.contrib.auth.models import User
from Oauth.models import TeacherProfile
# Create your models here.
class Departments(models.Model):
    head_of_department = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE)
    department_name = models.CharField(max_length = 191)
    starting_year = models.CharField(max_length = 191)
    student_capacity = models.CharField(max_length = 191)
    department_details = models.TextField(max_length = 191)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.department_name} : {self.head_of_department} Department'