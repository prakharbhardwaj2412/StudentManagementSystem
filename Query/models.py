from django.db import models
from Student.models import Student_table

# Create your models here.
class Query_table(models.Model):
	"""docstring for Query_table"""
	STUDENT = models.ForeignKey(Student_table, on_delete=models.CASCADE)
	QUERY_SUBJECT = models.CharField(max_length=500)
	QUERY_TEXT = models.CharField(max_length=500)
	DATE = models.CharField(max_length=50)
	TIME = models.CharField(max_length=50)
	STATUS = models.CharField(max_length=25)