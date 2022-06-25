
from secrets import choice
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    name= models.CharField(max_length=50,null=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=10,validators=[MinLengthValidator(10)],null=True)
    gender=models.CharField(max_length=50,choices=(("Male","Male"),("Female","Female"),("Other","Other")))
    country=models.CharField(max_length=50,null=True)
    experience=models.CharField(max_length=50,null=True)
    role=models.CharField(max_length=50,choices=((
        ("Teacher","Teacher"),
        ("Student","Student"))))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email