from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField()
    gpa = models.FloatField()

    def __str__ (self):
        return str(self.firstname) + " " + str(self.lastname)
