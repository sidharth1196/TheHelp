from django.shortcuts import render
from Home.models import Work

# Create your views here.

def index(request):
    works = Work.objects.all()
    return render(request, 'Home/home.html', {'works':works})