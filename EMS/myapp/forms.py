from django import forms
from datetime import date
from .models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm, UserChangeForm, PasswordResetForm
from django.utils.translation import gettext_lazy as _

# class DateInput(form.DateInupt):
#     input_type = 'date'
# Signup Form Starts Here -->


class SignUpFrom(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        age = (date.today() - dob).days / 365
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old')
        return dob
    def clean_first_name(self):
        fn = self.cleaned_data['first_name'].capfirst()
        return fn

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "employee_id", "mobile_number", "date_of_birth",
                  "gender", "emp_ctc", "manager_name", "department", "remarks", "emp_cv", "emp_images",)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'emp_ctc': forms.NumberInput(attrs={'class': 'form-control'}),
            'manager_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'emp_cv': forms.FileInput(attrs={'class': 'form-control'}),
            'emp_images': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(),
        }


# Login Form Starts here -->
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )

# Change Password Form Starts Here -->


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )


class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile_number',
                  'department', 'manager_name', 'gender', 'remarks', 'emp_images', 'emp_cv']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'manager_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'emp_cv': forms.FileInput(attrs={'class': 'form-control'}),
            'emp_images': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(),
        }
