from Student.models import Student_table
from .models import Query_table
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

# insert_query() is to raise query by student. Student can raise the query if the status of his last query is not pending
def insert_query(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		print("$$$$$$$")
		print(obj)
		if not (Query_table.objects.filter(STUDENT_id=obj['STUDENT'], STATUS="pending")).exists():
			query = Query_table.objects.create(STUDENT_id= obj['STUDENT'], QUERY_SUBJECT= obj['QUERY_SUBJECT'], QUERY_TEXT= obj['QUERY_TEXT'])
			return JsonResponse("query inserted", safe=False)
		else:
			return JsonResponse("Query status is still pending.", safe=False)
		
# query_list() displays the list of all queries made by students
def query_list(request):
	if (request.method=="GET"):
		query= Query_table.objects.filter(STATUS="pending")
		detail=query.values('id', 'STUDENT', 'QUERY_SUBJECT', 'QUERY_TEXT', 'DATE')
		return JsonResponse(list(detail), safe=False)

# query_response() changes the status of a particular query as approved or rejected
def query_response(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		print(obj)
		updated_query= Query_table.objects.filter(STUDENT_id=obj['STUDENT']).update(STATUS=obj['STATUS'])
		return JsonResponse("Query has been answered", safe=False)