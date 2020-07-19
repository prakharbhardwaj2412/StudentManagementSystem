from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Teacher_table
from Student.models import Student_table
import json
from django.db.models import Q
# Create your views here.

# login() functions checks the username and password for both student and teacher
def login(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		a=Teacher_table.objects.filter(TEACHER_USERNAME=obj['username'], PASSWORD=obj['password'])
		b=Student_table.objects.filter(USERNAME=obj['username'], PASSWORD=obj['password'])
		if a.exists():
			messsage=json.dumps({"id": a[0].id, "type": "teacher"})
		elif b.exists():
			messsage=json.dumps({"id": b[0].id, "type": "student"})
				
		else:
			messsage="wrong credientials"
		return JsonResponse(messsage, safe=False)	


# student_list() returns the list of all students with status=active
def student_list(request):
	if (request.method=="GET"):
		student= Student_table.objects.filter(STATUS="active")
		detail=student.values('id', 'FIRST_NAME', 'LAST_NAME', 'USERNAME', 'EMAIL', 'CONTACT', 'BRANCH', 'YEAR')
		return JsonResponse(list(detail), safe=False)

# view_student() returns the details of a particular student 
def view_student(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		student= Student_table.objects.filter(id=obj['id'])
		detail= student.values('id', 'FIRST_NAME', 'LAST_NAME', 'USERNAME', 'EMAIL', 'CONTACT', 'BRANCH', 'YEAR')
		return JsonResponse(list(detail), safe=False)
		
	

# insert_student() creates a new student
def insert_student(request):
	if (request.method=="POST"):
		detail=json.loads(request.body)
		if not Student_table.objects.filter(Q(USERNAME= detail['USERNAME']) | Q(EMAIL=detail['EMAIL'])).exists():
			info = Student_table.objects.create(**detail)
			# info.save()
			return JsonResponse("entry successful", safe=False)
		else:
			return JsonResponse("Student Exist", safe=False)

# update_student() update details of student
def update_student(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		print(obj)
		if Student_table.objects.filter(id=obj['id']).exists():
			Student_table.objects.filter(id=obj['id']).update(**obj)
			return JsonResponse("Update Successful", safe=False)
		else:
			return JsonResponse("Update Unsuccessful", safe=False)

# delete_student() changes the status of student to inactive
def delete_student(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		info = Student_table.objects.filter(id=obj['id']).update(STATUS='inactive')
		return JsonResponse("Student Deleted", safe=False)
