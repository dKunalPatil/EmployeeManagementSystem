from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpFrom, LoginForm, ChangePasswordForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib import messages
import datetime
# Email ka Zamaa-->
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Zamaa Ends Here


# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpFrom(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                messages.success(
                    request, "Your Account has been Successfully Created !!")
                return redirect('/')
        else:
            fm = SignUpFrom()
        return render(request, 'myapp/signup.html', {'form': fm})
    else:
        messages.error(request, "Already Logged In!!")
        return redirect('/profile/')


def age_calculate(date):
    # return (datetime.today().date - date).days/365
    return int((datetime.date.today() - date).days / 365.25)


def profile(request):
    if request.user.is_authenticated:
        dob = request.user.date_of_birth
        age = age_calculate(dob)
        # messages.success(request, "You are Logged In Successfully !!")
        return render(request, 'myapp/profile.html', {'emp': age})
    else:
        return redirect('/login/')


def user_logout(request):
    logout(request)
    return redirect('/login/')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'

# class PasswordResetView(auth_views.PasswordResetView):
#     template_name = 'myapp/resetpass.html'
#     email_template_name = 'myapp/resetpassdone.html'
#     success_url = '/resetpassdone/'

# class PasswordChangeDoneView(auth_views.PasswordResetDoneView):
#     template_name = 'myapp/resetpassdone.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'myapp/changepass.html'
    success_url = '/changepassdone/'


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'myapp/changepassdone.html'

# Password Reser Starts Here -->


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            # associated_users = User.objects.filter(email=data)
            associated_users = User.objects.filter(Q(email=data))
            print(associated_users)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "myapp/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="myapp/password_reset.html", context={"password_reset_form": password_reset_form})
