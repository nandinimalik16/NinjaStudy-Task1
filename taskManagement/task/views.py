from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logout

from .models import CustomUser
from .forms import *
# Create your views here.
def index(request):
    return redirect('/home')
def homePage(request):
    try:
        if request.user.is_authenticated:
            print(request.user)
            print("yes authenticated")
    except:
        pass
    return render(request,'index.html',{})

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

def login(request):
    if request.method=="POST":
        form=loginForm(request.POST)
        if form.is_valid():
            print(request.POST)
            try:
                user=CustomUser.objects.get(phone=form.cleaned_data['username_field'])
                form.cleaned_data['username_field']=user.email
            except CustomUser.DoesNotExist:
                pass
            print(form.cleaned_data)
            user=authenticate(email=form.cleaned_data['username_field'],password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request,user)
                if user.role=="Teacher":
                    return HttpResponseRedirect(f'/teacher/dashboard/{user.id}')
                else:
                    return HttpResponseRedirect(f'/student/dashboard/{user.id}')
            else:
                return HttpResponseRedirect('/login/')

    return render(request,'login.html',{})

def logout(request):
    auth_logout(request)

@login_required(redirect_field_name='/login/')
def studentDashboard(request,pk):
    if(request.user.id!=pk or request.user.role!='Student'):
        return HttpResponse('Unauthorized', status=401)
    return HttpResponse('')

@login_required(redirect_field_name='/login/')
def teacherDashboard(request,pk):
    if(request.user.id!=pk or request.user.role!='Teacher'):
        return HttpResponse('Unauthorized', status=401)
    return HttpResponse('')

