from django.urls import path

from . import views

urlpatterns = [

	# student/password-update
    path('password-update/', views.password_update, name='password-update'),
]