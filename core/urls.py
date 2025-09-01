# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('check_company/', views.check_company, name="check_company"),
]
