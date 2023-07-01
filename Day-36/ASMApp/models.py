from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	rt = [
		(0,'Guest'),
		(1,'Student'),
		(2,'Teacher'),
	]
	role_type = models.IntegerField(default=0)
	
