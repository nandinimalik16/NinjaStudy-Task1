from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import *
# Create your views here.
def index(request):
    return redirect('/home')
def homePage(request):
    return render(request,'index.html',{})

def login(request):
    return render(request,'login.html',{})

def studentSignup(request):
    if request.method=="POST":
        print(request.POST)
        form=studentRegistrationForm(request.POST)
        if form.is_valid():
            user=CustomUser()
            user.name=form.cleaned_data['name']
            user.email=form.cleaned_data['email']
            user.phone=form.cleaned_data['phone']
            user.gender=form.cleaned_data['gender']
            user.country=form.cleaned_data['country']
            user.set_password(form.cleaned_data['password'])
            user.role='Student'
            user.save()
            return HttpResponseRedirect('/login/')
        print(form.errors)
    return render(request,'studentSignUp.html',{})

def teacherSignup(request):
    if request.method=="POST":
        form=teacherRegistrationForm(request.POST)
        if form.is_valid():
            user=CustomUser()
            user.name=form.cleaned_data['name']
            user.email=form.cleaned_data['email']
            user.phone=form.cleaned_data['phone']
            user.gender=form.cleaned_data['gender']
            user.country=form.cleaned_data['country']
            user.set_password(form.cleaned_data['password'])
            user.experience=form.cleaned_data['experience']
            user.role='Teacher'
            user.save()
            return HttpResponseRedirect('/login/')
        print(form.errors)
    return render(request,'teacherSignUp.html',{})