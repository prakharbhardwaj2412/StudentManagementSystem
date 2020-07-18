from django.db import models

# Create your models here.

class Student_table(models.Model):
	"""docstring for Student_table"""
	FIRST_NAME = models.CharField(max_length=250)
	LAST_NAME = models.CharField(max_length=250)
	USERNAME = models.CharField(max_length=250, unique=True)
	EMAIL = models.CharField(max_length=250, unique=True)
	CONTACT = models.CharField(max_length=250)
	BRANCH = models.CharField(max_length=250)
	YEAR = models.CharField(max_length=250)
	PASSWORD = models.CharField(max_length=250, default='STUDENT')
	STATUS = models.CharField(max_length=25, default='active')

	