from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from delivery.models import Company
from .forms import RegisterUserForm
from .forms import RegisterClientForm

def registerclient(request, company_id):
    company = Company.objects.get(pk = company_id)
    if request.method == 'POST':
        user = RegisterUserForm(request.POST)
        client = RegisterClientForm(request.POST)
        if user.is_valid and client.is_valid:
            newuser = user.save()
            newclient = client.save(commit=False)
            newclient.user = newuser
            newclient.company = company
            newclient.save()
            newuser.groups.add(Group.objects.get(name='Client'))
            return redirect('/client/login')
    else:
        user = RegisterUserForm()
        client = RegisterClientForm()
    context = {'company': company, 'user': user, 'client': client}
    return render(request, 'client/registerclient.html', context)
    
def loginclient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'client/placejob.html')

    return render(request, 'client/login.html')

def placejob(request):
    return render(request, 'client/placejob.html')

def viewstatus(request):
    return render(request, 'client/viewstatus.html')

def viewhistory(request):
    return render(request, 'client/viewhistory.html')
    
