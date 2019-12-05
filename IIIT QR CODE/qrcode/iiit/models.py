from django.db import models

# Create your models here.
class userinput(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    scholar_no=models.CharField(max_length=8)
    year=models.CharField(max_length=1)
    branch=models.CharField(max_length=3)
    def __str__(self):
        return self.fname