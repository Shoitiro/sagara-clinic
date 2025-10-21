from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('facility/', views.facility, name='facility'),
    path('services/', views.services, name='services'),
    path('access/', views.access, name='access'),
    path('news/', views.news, name='news'),
    path('reservation/', views.reservation, name='reservation'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
]