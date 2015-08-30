from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterCompanyForm

def index(request):
    return render(request, 'company/index.html')

def registercompany(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        company = RegisterCompanyForm(request.POST)
        if user.is_valid() and company.is_valid:
            user.save()
            company.save()
            return render(request, 'company/admin.html/')
    else:
        user = UserCreationForm()
        company = RegisterCompanyForm()
        
    context = {'user': user, 'company': company}
    return render(request, 'company/registercompany.html', context)

def admin(request):
    return render(request, 'company/admin.html')
