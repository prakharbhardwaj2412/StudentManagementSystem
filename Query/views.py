from Student.models import Student_table
from .models import Query_table
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.


def insert_query(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		print("$$$$$$$")
		print(obj)
		student_obj=list(Student_table.objects.filter(id= obj['STUDENT']).values())
		print(student_obj[0]['id'])
		query = Query_table.objects.create(STUDENT= student_obj[0]['id'], QUERY_SUBJECT= obj['QUERY_SUBJECT'], QUERY_TEXT= obj['QUERY_TEXT'])
		return JsonResponse("query inserted", safe=False)



		# if (Query_table.objects.filter(STUDENT=obj['student-id'], STATUS="pending")).exists():
		# 	
		# else:
		# 	return JsonResponse("Query status is still pending.")
		
def query_list(request):
	if (request.method=="GET"):
		query= Query_table.objects.filter(STATUS="pending")
		detail=query.values('id', 'STUDENT', 'QUERY_SUBJECT', 'QUERY_TEXT', 'DATE')
		return JsonResponse(list(detail), safe=False)

def query_response(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		updated_query= Query_table.objects.filter(id=obj['id']).update(STATUS=obj['status'])
		return JsonResponse("Query has been answered", safe=False)