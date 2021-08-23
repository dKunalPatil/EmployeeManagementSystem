from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    employee_id = models.IntegerField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    emp_ctc = models.IntegerField(null=True)
    manager_name = models.CharField(max_length=150, null=True, blank=True)
    date_of_exit = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    emp_cv = models.FileField(upload_to='emp_cv', blank=True)
    emp_images = models.ImageField(upload_to='emp_images', blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()