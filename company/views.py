from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from .forms import RegisterCompanyForm
from .forms import RegisterCourierForm
from .forms import RegisterUserForm
from delivery.models import Courier
from delivery.models import Company
from delivery.forms import PlaceJobForm

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('/delivery/jobboard/')

    return render(request, 'company/login.html')

def registercompany(request):
    if request.method == 'POST':
        user = RegisterUserForm(request.POST)
        company = RegisterCompanyForm(request.POST)
        courier = RegisterCourierForm(request.POST)

        try:
            if user.is_valid() and company.is_valid:
                newuser = user.save()
                newcompany = company.save()
                newcourier = courier.save(commit=False)
                newcourier.user = newuser
                newcourier.save()
                newuser.groups.add(Group.objects.get(name='CompanyAdmin'))
                newcourier.companies.add(newcompany)
                return redirect('/company/login/')

        except ValueError:
            pass
            
    else:
        user = RegisterUserForm()
        company = RegisterCompanyForm()
        courier = RegisterCourierForm()
        
    context = {'user': user, 'company': company, 'courier': courier}
    return render(request, 'company/registercompany.html', context)

@login_required()
def admin(request):
    return render(request, 'company/admin.html')

@login_required()
def canceljob(request):
    return render(request, 'delivery/jobboard')

@login_required()
def registercourier(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        user = Courier.objects.filter(user = user_id)
        company = Company.objects.filter(courier = user)
        userform = RegisterUserForm(request.POST)
        courierform = RegisterCourierForm(request.POST)

        try:
            if userform.is_valid() and courierform.is_valid():
                newuser = userform.save()
                newcourier = courierform.save(commit=False)
                newcourier.user = newuser
                newcourier.save()
                newuser.groups.add(Group.objects.get(name='Courier'))
                for c in company:
                    newcourier.companies.add(c)
                return redirect('/delivery/jobboard/')

        except ValueError:
            pass
            
    else:
        userform = RegisterUserForm()
        courierform = RegisterCourierForm()
        
    context = {'user': userform, 'courier': courierform}
    return render(request, 'company/registercompany.html', context)

#Needs Work    
def assigncourier(request):
    if request.method == 'POST':

        try:
            
            return redirect('/delivery/jobboard/')

        except ValueError:
            pass
        
    else:
        user_id = request.session['user_id']
        courier = Courier.objects.filter(user = user_id)
        company = Company.objects.filter(courier = courier)
        roster = Courier.objects.filter(companies = company)

    context = {'roster': roster}
    return render(request, 'company/assigncourier.html', context)

@login_required()
def listcouriers(request):
    user_id = request.session['user_id']
    courier = Courier.objects.filter(user = user_id)
    company = Company.objects.filter(courier = courier)
    roster = Courier.objects.filter(companies = company)
    context = {'roster': roster}
    return render(request, 'company/listcouriers.html', context)

@login_required()
def courierdetails(request, courier_id):
    details = Courier.objects.get(pk = courier_id)
    context = {'details': details}
    return render(request, 'company/courierdetails.html', context)

@login_required()
def placejob(request):
    if request.method == 'POST':
        job = PlaceJobForm(request.POST)
        if job.is_valid:
            user_id = request.session['user_id']
            courier = Courier.objects.get(user = user_id)
            company = Company.objects.get(courier = courier)
            request.session['company_id'] = company.id
            try:
                newjob = job.save(commit = False)
                newjob.company = company
                newjob.status = 'UNASSIGNED'
                newjob.save()
                print '6'
                return redirect('/delivery/jobboard/')

            except ValueError:
                pass
                
    else:
        job = PlaceJobForm()
    
    context = {'job': job}
    return render(request, 'company/placejob.html', context)
