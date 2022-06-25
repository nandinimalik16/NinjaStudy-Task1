from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return redirect('/home')
def homePage(request):
    return render(request,'index.html',{})

def studentSignup(request):
    return render(request,'studentSignUp.html',{})

def teacherSignup(request):
    return render(request,'teacherSignUp.html',{})

def login(request):
    return render(request,'login.html',{})
