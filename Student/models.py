from django.db import models

# Create your models here.

class Student_table(models.Model):
	"""docstring for Student_table"""
	FIRST_NAME = models.CharField(max_length=250, blank=False)
	LAST_NAME = models.CharField(max_length=250, blank=False)
	USERNAME = models.CharField(max_length=250, blank=False, unique=True)
	EMAIL = models.EmailField(max_length=250, blank=False)
	CONTACT = models.CharField(max_length=250, blank=False)
	BRANCH = models.CharField(max_length=250, blank=False)
	YEAR = models.CharField(max_length=250, blank=False)
	PASSWORD = models.CharField(max_length=250, blank=False, default='STUDENT')
	STSTUS = models.CharField(max_length=25, default='active')

	