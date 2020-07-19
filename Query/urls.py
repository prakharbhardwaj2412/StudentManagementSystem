from django.urls import path

from . import views

urlpatterns = [
	
	# query/insert-query/
	path('insert-query/', views.insert_query, name="insert-query"),

	# query/query-list/
	path('query-list/', views.query_list, name="query-list"),

	# query/query-view/
	path('query-view/', views.query_view, name="query-view"),

	# query/query-view/student
	path('query-view/student/', views.query_view_student, name="query-view-student"),


	# query/query-response/
	path('query-response/', views.query_response, name="query-response"),


]