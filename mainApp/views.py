from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/index.html')

def resume(request):
	return render(request, 'mainApp/resume.html')

def contact(request):
	return render(request, 'mainApp/contact.html')