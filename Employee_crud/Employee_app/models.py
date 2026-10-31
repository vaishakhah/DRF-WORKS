from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=30)
    Emp_id = models.IntegerField()
    Age = models.IntegerField()
    Place = models.CharField(max_length=30)
    mode_choices =(('male','male'),('female','female'))
    Gender = models.CharField(max_length=30,choices=mode_choices)
    Joining_date = models.DateField(auto_now_add=True)
    Salary = models.FloatField()
    Designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to="employee",null=True,blank=True)

