from django.db import models
from django.db import models
# Create your models here.


class Employee(models.Model):

    empid = models.IntegerField()

    name = models.CharField(max_length=100)

    deptname = models.CharField(max_length=100)

    salary = models.IntegerField()

    designation = models.CharField(max_length=100)

    image = models.ImageField(upload_to='employees')

    def __str__(self):
        return self.name