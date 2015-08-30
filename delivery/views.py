from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Job

def index(request):
    return render(request, 'delivery/index.html')

def jobboard(request):
    jobs = Job.objects.all().prefetch_related('client')
    context = {'jobs': jobs}
    return render(request, 'delivery/jobboard.html', context)

def jobdetails(request, job_id):
    details = get_object_or_404(Job.objects.get(pk = job_id))
    context = {'details': details}
    return render(request, 'delivery/jobdetails.html', context)
