from django.db import models

# Create your models here.

class Student(models.Model):
	sroll = models.CharField(max_length=15)
	sname = models.CharField(max_length=30)
	syear = models.CharField(max_length=5)
	sbranch = models.CharField(max_length=50)
	sage = models.IntegerField(default=18)
