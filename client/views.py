from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from delivery.models import Company
from delivery.models import Client
from .forms import RegisterUserForm
from .forms import RegisterClientForm
from .forms import PlaceJobForm

def registerclient(request, company_id):
    company = Company.objects.get(pk = company_id)
    
    if request.method == 'POST':
        user = RegisterUserForm(request.POST)
        client = RegisterClientForm(request.POST)
        
        try:
            if user.is_valid and client.is_valid:
                newuser = user.save()
                newclient = client.save(commit = False)
                newclient.user = newuser
                newclient.company = company
                newclient.save()
                newuser.groups.add(Group.objects.get(name='Client'))
                return redirect('/client/login/')
            
        except ValueError:
            pass

    else:
        user = RegisterUserForm()
        client = RegisterClientForm()
        
    context = {'company': company, 'user': user, 'client': client}
    return render(request, 'client/registerclient.html', context)
    
def loginclient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('/client/homepage/')

    return render(request, 'client/login.html')

def homepage(request):
    return render(request, 'client/homepage.html')

@login_required()
def placejob(request):
    if request.method == 'POST':
        job = PlaceJobForm(request.POST)
        if job.is_valid:
            user_id = request.session['user_id']
            client = Client.objects.get(user = user_id)
            company = Company.objects.get(client = client)
            request.session['client_id'] = client.id
            request.session['company_id'] = company.id
            
            try:
                newjob = job.save(commit = False)
                newjob.company = company
                newjob.client = client
                newjob.status = 'UNASSIGNED'
                newjob.save()
                return render(request, 'client/homepage.html')

            except ValueError:
                pass
                
    else:
        job = PlaceJobForm()

    context = {'job': job}
    return render(request, 'client/placejob.html', context)

@login_required()
def viewstatus(request):
    return render(request, 'client/viewstatus.html')

@login_required()
def viewhistory(request):
    return render(request, 'client/viewhistory.html')
    
