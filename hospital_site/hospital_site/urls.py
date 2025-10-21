"""
URL configuration for hospital_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import (
    home, staff, facility, services, access,
    news, reservation, questionnaire
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('staff/', staff, name='staff'),
    path('facility/', facility, name='facility'),
    path('services/', services, name='services'),
    path('access/', access, name='access'),
    path('news/', news, name='news'),
    path('reservation/', reservation, name='reservation'),
    path('questionnaire/', questionnaire, name='questionnaire'),
]

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # ← これが main/urls.py を読み込む
]