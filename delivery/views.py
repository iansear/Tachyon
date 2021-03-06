from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Courier
from .models import Company
from .models import Job
from .forms import PlaceJobForm

def index(request):
    return render(request, 'delivery/index.html')

@login_required()
def jobboard(request):
    user_id = request.session['user_id']
    courier = Courier.objects.filter(user = user_id)
    company = Company.objects.filter(courier = courier)
    jobs = Job.objects.filter(company = company)
    riders = Courier.objects.filter(companies = company)
    context = {'jobs': jobs, 'user_id': user_id, 'courier': courier,
               'company': company, 'riders': riders}
    return render(request, 'delivery/jobboard.html', context)

@login_required()
def jobdetails(request, job_id):
    details = Job.objects.get(pk = job_id)
    context = {'details': details}
    return render(request, 'delivery/jobdetails.html', context)
