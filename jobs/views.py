from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    #Grabs everything from the database.
    jobs = Job.objects
    return render(request, 'job_temps/home.html',{'jobs': jobs})
