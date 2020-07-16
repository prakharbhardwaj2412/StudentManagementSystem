from django.db import models

# Create your models here.

class Teacher_table(models.Model):
	"""docstring for Teacher_table"""
	TEACHER_USERNAME = models.CharField(max_length=250, blank=False)
	PASSWORD = models.CharField(max_length=250, blank=False)