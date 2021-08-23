from django.shortcuts import render, redirect
from .forms import SignUpFrom, LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
import datetime
# Create your views here.

def user_signup(request):
    if request.method == 'POST':
        fm = SignUpFrom(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = SignUpFrom()
    return render(request, 'myapp/signup.html', {'form':fm})

def age_calculate(date):
    # return (datetime.today().date - date).days/365
    return int((datetime.date.today() - date).days / 365.25)


def profile(request):
    if request.user.is_authenticated:
        dob = request.user.date_of_birth
        age = age_calculate(dob)
        return render(request, 'myapp/profile.html', {'emp': age})
    else:
        return redirect('/login/')

def user_logout(request):
    logout(request)
    return redirect('/login/')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'

class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'myapp/changepass.html'
    success_url = '/changepassdone/'

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'myapp/changepassdone.html'