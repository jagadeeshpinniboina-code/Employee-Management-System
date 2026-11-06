from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.BigIntegerField(unique=True)
    department=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    salary=models.FloatField()
    city=models.CharField(max_length=30)
    status=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'

