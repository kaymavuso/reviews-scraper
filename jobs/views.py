from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Job
from .forms import JobForm

# Create your views here.

def jobs(request):
    jobs = Job.objects.all()
    all_jobs = { 'jobs': jobs }
    return render(request, 'jobs/jobs.html', all_jobs)

def job(request, primary_key):
    single_job = Job.objects.get(id=primary_key)
    return render(request, 'jobs/single-job.html', {'single_job': single_job})

@login_required(login_url="login")
def createScrapeJob(request):
    profile = request.user.profile
    form = JobForm()

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            # we could have did form.save here but chose to no commit
            # until we have forced the userprofile to be the job owner
            job = form.save(commit=False)
            job.owner = profile
            job.save()
               
            return redirect('jobs')

    form_contents = { 'form': form }
    return render(request, 'jobs/job_form.html', form_contents)

@login_required(login_url="login")
def updateScrapeJob(request, primary_key):
    job = Job.objects.get(id=primary_key)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')

    form_contents = {'form': form, 'job': job}
    return render(request, 'jobs/job_form.html', form_contents)

@login_required(login_url="login")
def deleteScrapeJob(request, primary_key):
    job = Job.objects.get(id=primary_key)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs')
    job_object = {'object': job}
    return render(request, 'jobs/generic_delete_template.html', job_object)

# video 17 24:06