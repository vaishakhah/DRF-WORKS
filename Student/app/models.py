from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Course = models.CharField(max_length=30)
    Marks = models.IntegerField()
class Course(models.Model):
    mode_choices=(('offline','offline'),('online','online'))
    Course_name = models.CharField(max_length=30)
    Fee = models.FloatField()
    Duration = models.CharField(max_length=30)
    Instructor = models.CharField(max_length=30)
    Mode = models.CharField(choices=mode_choices)
