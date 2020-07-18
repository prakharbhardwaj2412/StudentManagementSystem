from django.urls import path

from . import views

urlpatterns = [

	# teacher/login/
	path('login/', views.login, name="login"),

	# teacher/student-list/
	path('student-list/', views.student_list, name="student-list"),

	# teacher/insert-student/
	path('insert-student/', views.insert_student, name="insert-student"),

	# teacher/view-student/
	path('view-student/', views.view_student, name="view-student"),

	# teacher/update-student/
	path('update-student/', views.update_student, name="update-student"),

	# teacher/delete-student/
	path('delete-student/', views.delete_student, name="delete-student"),

	

]