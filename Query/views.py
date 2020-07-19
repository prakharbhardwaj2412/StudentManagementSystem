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
		detail=query.values('id', 'STUDENT', 'QUERY_SUBJECT', 'DATE', 'STUDENT__FIRST_NAME', 'STUDENT__LAST_NAME', 'STUDENT__BRANCH', 'STUDENT__YEAR')
		return JsonResponse(list(detail), safe=False)

# query_view() displays particular query
def query_view(request):
	if (request.method=="POST"):
		id_obj=json.loads(request.body)
		print(id_obj)
		query= Query_table.objects.filter(id=id_obj["id"])
		detail=query.values('id', 'STUDENT', 'STUDENT__FIRST_NAME', 'STUDENT__LAST_NAME', 'QUERY_SUBJECT', 'QUERY_TEXT', 'DATE', 'STUDENT__BRANCH', 'STUDENT__YEAR')
		return JsonResponse(list(detail), safe=False)

# query_view_student() displays particular query
def query_view_student(request):
	if (request.method=="POST"):
		id_obj=json.loads(request.body)
		print(id_obj)
		query= Query_table.objects.filter(STUDENT=id_obj["id"])
		detail=query.values('id', 'QUERY_SUBJECT', 'QUERY_TEXT','REPLY', 'STATUS')
		print(detail)
		return JsonResponse(list(detail), safe=False)



# query_response() changes the status of a particular query as approved or rejected
def query_response(request):
	if (request.method=="POST"):
		obj=json.loads(request.body)
		print(obj)
		updated_query= Query_table.objects.filter(id=obj['id']).update(STATUS=obj['STATUS'], REPLY=obj['REPLY'])
		return JsonResponse("Query has been answered", safe=False)