# company_checker/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Company Checker 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('',include('core.urls')
]
