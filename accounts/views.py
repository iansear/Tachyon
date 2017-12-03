from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required()
def logoutuser(request):
    logout(request)
    return redirect('/tachyoncouriersystems/')
