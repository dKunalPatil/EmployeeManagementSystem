from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _

# class DateInput(form.DateInupt):
#     input_type = 'date'

class SignUpFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "employee_id", "date_of_birth", "emp_ctc", "manager_name",
                  "date_of_exit", "department", "remarks", "emp_cv", "emp_images",)

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )