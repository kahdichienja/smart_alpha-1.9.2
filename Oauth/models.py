from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 191, blank=True, null=True)
    last_name = models.CharField(max_length = 191, blank=True, null=True)
    mobile_number = models.CharField(max_length = 191, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='teacher_profile')
    joined_date = models.CharField(max_length = 191, blank=True, null=True)
    department = models.CharField(max_length = 191, blank=True, null=True)
    designation = models.CharField(max_length = 191, blank=True, null=True)
    gender = models.CharField(max_length = 191, blank=True, null=True)
    email = models.EmailField()
    dob = models.CharField(max_length = 191, blank=True, null=True)
    address = models.TextField()
    education = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.mobile_number}: {self.email}'