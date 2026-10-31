from django.db import models



# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    mode_choices = (
    ("cardiology", "Cardiology"),
    ("dermatology", "Dermatology"),
    ("endocrinology", "Endocrinology"),
    ("ent", "Ear, Nose & Throat (ENT)"),
    ("gastroenterology", "Gastroenterology"),
    ("generalmedicine", "General Medicine / Internal Medicine"),
    ("general_surgery", "General Surgery"),
    ("gynecology", "Gynecology & Obstetrics"),
    ("hematology", "Hematology"),
    ("nephrology", "Nephrology"),
    ("neurology", "Neurology"),
    ("oncology", "Oncology"),
    ("ophthalmology", "Ophthalmology"),
    ("orthopedics", "Orthopedics"),
    ("pediatrics", "Pediatrics"),
    ("psychiatry", "Psychiatry"),
    ("pulmonology", "Pulmonology"),
    ("radiology", "Radiology"),
    ("urology", "Urology"),
    ("other", "Other"),
)
    specification = models.CharField(choices=mode_choices)
    fee = models.IntegerField()
    qualification = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
