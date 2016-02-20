from django.shortcuts import render
from delivery.models import Company

def mainpage(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'tachyoncouriersystems/mainpage.html', context)

