from django.shortcuts import render
from .forms import ReservationForm
from .forms import QuestionnaireForm

def questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            return render(request, 'main/questionnaire_done.html', {'form': form})
    else:
        form = QuestionnaireForm()
    return render(request, 'main/questionnaire.html', {'form': form})


def home(request):
    return render(request, 'main/home.html')

def staff(request):
    return render(request, 'main/staff.html')

def facility(request):
    return render(request, 'main/facility.html')

def services(request):
    return render(request, 'main/services.html')

def access(request):
    return render(request, 'main/access.html')

def news(request):
    return render(request, 'main/news.html')

def questionnaire(request):
    return render(request, 'main/questionnaire.html')

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            return render(request, 'main/reservation_done.html', {'form': form})
    else:
        form = ReservationForm()
    return render(request, 'main/reservation.html', {'form': form})