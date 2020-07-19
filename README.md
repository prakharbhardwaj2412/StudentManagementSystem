# StudentManagementSystem
Student Mangement System for schools and colleges


BACKEND URLS AND JSONS

Teacher Dashboard:
Login: teacher/login/
Json from frontend: { “username”: value, “password”:value}

Student list:  teacher/student-list/ [GET]

Create Student: teacher/insert-student/
Json from frontend: {		"first_name": "value",
				"last_name": "value",
				"username": "value",
				"email": "value",
				"contact": "value",
				"branch": “value",
				"year": “value”	}

View Student: teacher/view-student
Json from frontend: {	“id”: “value”		}

Update Student: teacher/update-student/
Json from frontend: {		“id”: “ value”,
				"first_name": "value",
				"last_name": "value",
				"username": "value",
				"email": "value",
				"contact": "value",
				"branch": “value",
				"year": “value”	}

Delete Student: teacher/delete-student/
Json from frontend: {	“id”: “value”		}

Query-list: query/query-list [GET]

Query response from teacher: query/query-response
Json from frontend: {		“STUDENT”: “value”,
				“STATUS”: “value”	}





Student Dashboard:
Insert-Query: query/insert-query
Json from frontend: {	 	“STUDENT”: “value”,
				“QUERY_SUBJECT”: “value”,
				“QUERY_TEXT”: “value”	}

Password Updation: student/password-update/
Json from frontend: {	“id”: “value”,
				“password”: “value”	}

