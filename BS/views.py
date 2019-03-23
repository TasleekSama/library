from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, 'BS/index.html')


def ar_books(request):
	return render(request, 'BS/ar_books.html')


def en_books(request):
	return render(request, 'BS/en_books.html')


def lib_tools(request):
	return render(request, 'BS/lib_tools.html')


def eng_tools(request):
	return render(request, 'BS/eng_tools.html')