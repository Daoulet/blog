from django.shortcuts import render

def index(request):
    return render (request, 'mainApp/homePage.html')

def contact(request):
    return render (request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, то задавайте их мне по телефону', '8777546231221221']})

def resume(request):
    return render (request, 'mainApp/resume.html')
