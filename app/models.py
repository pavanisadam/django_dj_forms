from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def _str_(self):
        return self.name

