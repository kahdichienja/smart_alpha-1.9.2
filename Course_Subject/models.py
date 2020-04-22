from django.db import models

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length = 191)
    subject_code = models.CharField(max_length = 191)
    subject_start = models.CharField(max_length = 191)
    subject_class = models.CharField(max_length = 191)
    subject_duration = models.CharField(max_length = 191)
    subject_hod = models.CharField(max_length = 191)
    subject_students_number = models.CharField(max_length = 191)
    subject_photo = models.ImageField(upload_to='subjects')
    subject_details = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f'{self.subject_name}'

class SubjectSyllabus(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    syllabus = models.TextField()

    def __str__(self):
        return f'{self.subject}: {self.syllabus}'

class SubjectObjective(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    objective = models.TextField()

    def __str__(self):
        return f'{self.subject}: {self.objective}'