
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
    phone = models.CharField(max_length=10,validators=[MinLengthValidator(10)],unique=True)
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

class Task(models.Model):
    task_id=models.AutoField(primary_key=True,auto_created=True)
    task_name=models.CharField(max_length=50)
    task_description=models.TextField()
    task_status=models.CharField(max_length=50,choices=(
        ("Initiate","Initiate"),
        ("Pending","Pending"),
        ("Completed","Completed"),
        ("OnHold","OnHold")
    ))
    creator_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

class TaskAssignment(models.Model):
    task_id=models.ForeignKey(Task,on_delete=models.CASCADE)
    student_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task_id.task_name}-{self.student_id.name}"
