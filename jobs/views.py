from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jobs(request):
    return render(request, 'jobs/jobs.html')

def job(request, primary_key):
    return render(request, 'jobs/single-job.html')