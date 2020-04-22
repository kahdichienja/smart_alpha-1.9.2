from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 191)
    last_name = models.CharField(max_length = 191)
    admission_number = models.CharField(max_length = 191)
    email = models.EmailField(blank=True, null=True)
    reg_date = models.CharField(max_length = 191)
    form_class = models.CharField(max_length=191)
    gender = models.CharField(max_length=191)
    mobile_number = models.CharField(max_length = 191, blank=True, null=True)
    parent_name = models.CharField(max_length = 191, blank=True, null=True)
    parent_mobile_number = models.CharField(max_length = 191, blank=True, null=True)
    dob = models.CharField(max_length = 191)
    address = models.TextField()
    student_photo = models.ImageField(upload_to='student_picture')
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{first_name} {last_name} : {admission_number}'
