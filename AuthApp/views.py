from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def home(request):
    status_var={
        "status1":"active"
    }
    
    return render(request, 'index.html', status_var)


def about_us(request):
    status_var={
        "status2":"active"
    }
    return render(request, 'about_us.html', status_var)

def login_user(request):
    status_var={
        "status3":"active"
    }
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/feeds')
        else:
            return redirect('/login')
        
    return render(request, 'login.html', status_var)

def signup(request):
    status_var={
        "status4":"active"
    }
    return render(request, 'signup.html', status_var)

def feeds(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'feeds.html')

def logout_user(request):
    logout(request)
    return redirect('/login')