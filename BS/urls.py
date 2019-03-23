from django.urls import path, re_path
from BS import views
from django.contrib.auth import views as auth_views

app_name = 'BS'

urlpatterns = [

	# urls:

	path('', views.index, name='index'),
	path('ar_books/', views.ar_books, name='ar_books'),
	path('en_books/', views.en_books, name='en_books'),
	path('lib_tools/', views.lib_tools, name='lib_tools'),
	path('eng_tools/', views.eng_tools, name='eng_tools'),

]