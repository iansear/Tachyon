from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from .forms import RegisterCompanyForm
from .forms import RegisterCourierForm
from .forms import RegisterUserForm

def index(request):
    return render(request, 'company/index.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session["user_id"] = user.id
                return redirect('/delivery/jobboard')

    return render(request, 'company/login.html')

def registercompany(request):
    if request.method == 'POST':
        user = RegisterUserForm(request.POST)
        company = RegisterCompanyForm(request.POST)
        courier = RegisterCourierForm(request.POST)
        if user.is_valid() and company.is_valid:
            newuser = user.save()
            newcompany = company.save()
            newcourier = courier.save()
            newuser.groups.add(Group.objects.get(name='CompanyAdmin'))
            newcourier.companies.add(newcompany)
            return redirect(request, '/company/login')
    else:
        user = RegisterUserForm()
        company = RegisterCompanyForm()
        courier = RegisterCourierForm()
        
    context = {'user': user, 'company': company, 'courier': courier}
    return render(request, 'company/registercompany.html', context)

def admin(request):
    return render(request, 'company/admin.html')
