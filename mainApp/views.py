from django.shortcuts import render

def index(request):
    return render (request, 'mainApp/homePage.html')

def contact(request):
    return render (request, 'mainApp/basic.html')

def resume(request):
    return render (request, 'mainApp/resume.html')
