from django.db import models

# Create your models here.

class Student(models.Model):
	y = [
		(1,'1st Year'),
		(2,'2nd Year'),
		(3,'3rd Year'),
		(4,'4th Year'),
	]
	b = [
		('0','Select Branch'),
		('CSE','Computer Science and Engineering'),
		('ECE','Electrical and Communication Engineering'),
	]
	sroll = models.CharField(max_length=15)
	sname = models.CharField(max_length=30)
	syear = models.IntegerField(max_length=2,default=1,choices=y)
	sbranch = models.CharField(max_length=5,default='0',choices=b)
	sage = models.IntegerField(null=True)

	def __str__(self):
		return self.sroll