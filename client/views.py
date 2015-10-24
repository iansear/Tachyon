from django.shortcuts import render

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
    
