from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Teacher_table
from Student.models import Student_table
import json
from django.db.models import Q
# Create your views here.

def login(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		print("########")
		print(obj)
		a=Teacher_table.objects.filter(TEACHER_USERNAME=obj['username'], PASSWORD=obj['password'])
		b=Student_table.objects.filter(USERNAME=obj['username'], PASSWORD=obj['password'])
		if a.exists():
			messsage=json.dumps({"id": a[0].id, "type": "teacher"})
		elif b.exists():
			messsage=json.dumps({"id": b[0].id, "type": "student"})
				
		else:
			messsage="wrong credientials"
		return JsonResponse(messsage, safe=False)	


def student_list(request):
	if (request.method=="GET"):
		student= Student_table.objects.filter(STATUS="active")
		detail=student.values('id', 'FIRST_NAME', 'LAST_NAME', 'USERNAME', 'EMAIL', 'CONTACT', 'BRANCH', 'YEAR')
		return JsonResponse(list(detail), safe=False)

def view_student(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		student= Student_table.objects.filter(id=obj['id'])
		detail= student.values('id', 'FIRST_NAME', 'LAST_NAME', 'USERNAME', 'EMAIL', 'CONTACT', 'BRANCH', 'YEAR')
		return JsonResponse(list(detail), safe=False)
		
	


def insert_student(request):
	if (request.method=="POST"):
		detail=json.loads(request.body)
		print("$$$$4")
		print(detail)
		if not Student_table.objects.filter(Q(USERNAME= detail['USERNAME']) | Q(EMAIL=detail['EMAIL'])).exists():
			info = Student_table.objects.create(**detail)
			# info.save()
			return JsonResponse("entry successful", safe=False)
		else:
			return JsonResponse("Student Exist", safe=False)

def update_student(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		print(obj)
		if Student_table.objects.filter(id=obj['id']).exists():
			Student_table.objects.filter(id=obj['id']).update(**obj)
			return JsonResponse("Update Successful", safe=False)
		else:
			return JsonResponse("Update Unsuccessful", safe=False)

		
def delete_student(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		info = Student_table.objects.filter(id=obj['id']).update(STATUS='inactive')
		return JsonResponse("Student Deleted", safe=False)
