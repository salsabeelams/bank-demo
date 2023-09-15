
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
