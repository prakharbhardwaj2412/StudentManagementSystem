from django.urls import path

from . import views

urlpatterns = [
	
	# query/insert-query/
	path('insert-query/', views.insert_query, name="insert-query"),

	# query/query-list/
	path('query-list/', views.query_list, name="query-list"),

	# query/query-response/
	path('query-response/', views.query_response, name="query-response"),


]