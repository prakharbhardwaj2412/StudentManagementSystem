from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json
from .models import Student_table




def password_update(request):
	if (request.method=="POST"):
		print(json.loads(request.body))
		obj=json.loads(request.body)
		if Student_table.objects.filter(id=obj['id']).exists():
			Student_table.objects.filter(id=obj['id']).update(PASSWORD=obj['password'])
			return JsonResponse("Password Update Successful", safe=False)
		else:
			return JsonResponse("Password Update Unsuccessful", safe=False)
