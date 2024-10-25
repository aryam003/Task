from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    ph_no = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name