# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def staff(request):
    return render(request, 'core/staff.html')

def facility(request):
    return render(request, 'core/facility.html')

def services(request):
    return render(request, 'core/services.html')

def access(request):
    return render(request, 'core/access.html')

def news(request):
    return render(request, 'core/news.html')

def reservation(request):
    return render(request, 'core/reservation.html')

def questionnaire(request):
    return render(request, 'core/questionnaire.html')
