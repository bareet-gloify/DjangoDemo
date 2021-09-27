from django.db import models

# Create your models here.
class employees(models.Model):
    firstName=models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    empId=models.IntegerField()

    def __str__(self):
        return self.firstName