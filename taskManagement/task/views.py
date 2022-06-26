from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logout

from .models import *
from .forms import *
# Create your views here.
def index(request):
    return redirect('/home')

def returnRedirect(user):
    if user.role=='Teacher':
        return redirect(f'/teacher/dashboard/{user.id}')
    else:
        return redirect(f'/student/dashboard/{user.id}')
def homePage(request):
    try:
        if request.user.is_authenticated:
            return returnRedirect(request.user)
    except:
        pass
    return render(request,'index.html',{})

def studentSignup(request):
    try:
        if request.user.is_authenticated:
            return returnRedirect(request.user)
    except:
        pass
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
    try:
        if request.user.is_authenticated:
            return returnRedirect(request.user)
    except:
        pass
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
    try:
        if request.user.is_authenticated:
            return returnRedirect(request.user)
    except:
        pass
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
    return redirect('/')

@login_required(redirect_field_name='/login/')
def studentDashboard(request,pk):
    if(request.user.id!=pk or request.user.role!='Student'):
        return HttpResponse('Unauthorized', status=401)
    taskAssignments=TaskAssignment.objects.filter(student_id=request.user)
    task_ids=[task.id for task in taskAssignments]
    tasks=Task.objects.filter(task_id__in=task_ids)
    return render(request,'studentDashboard.html',{"tasks":tasks,"name":request.user.name})

@login_required(redirect_field_name='/login/')
def teacherDashboard(request,pk):
    if(request.user.id!=pk or request.user.role!='Teacher'):
        return HttpResponse('Unauthorized', status=401)
    tasks=Task.objects.filter(creator_id=request.user)
    return render(request,'teacherDashboard.html',{"tasks":tasks,"name":request.user.name})

@login_required(redirect_field_name='/login/')
def createTask(request,pk):
    if(request.user.id!=pk or request.user.role!='Teacher'):
        return HttpResponse('Unauthorized', status=401)
    return render(request,'create.html')

@login_required(redirect_field_name='/login/')
def submitCreateTask(request,pk):
    if request.method=="POST":
        form=createTaskForm(request.POST)
        if form.is_valid():
            print("yes")
            task=Task()
            task.task_name=form.cleaned_data['task_name']
            task.task_description=form.cleaned_data['task_description']
            task.task_status=form.cleaned_data['task_status']
            task.creator_id=request.user
            task.save()
            return redirect(f'/teacher/dashboard/{pk}/')
    return redirect('create_task/')

@login_required(redirect_field_name='/login/')
def updateTask(request,pk,task_id):
    if(request.user.id!=pk or request.user.role!='Teacher'):
        return HttpResponse('Unauthorized', status=401)
    task=Task.objects.filter(task_id=task_id).values()[0]
    context={"task":task}
    return render(request,'update.html',context)

@login_required(redirect_field_name='/login/')
def submitUpdateTask(request,pk,task_id):
    if request.method=="POST":
        form=createTaskForm(request.POST)
        if form.is_valid():
            print("yes")
            task=Task.objects.get(task_id=task_id)
            task.task_name=form.cleaned_data['task_name']
            task.task_description=form.cleaned_data['task_description']
            task.task_status=form.cleaned_data['task_status']
            task.save()
            return redirect(f'/teacher/dashboard/{pk}/')
    return redirect('update_task/')

@login_required(redirect_field_name='/login/')
def viewTask(request,pk,task_id):
    if(request.user.id!=pk or request.user.role!='Teacher'):
        return HttpResponse('Unauthorized', status=401)
    
    tasks=TaskAssignment.objects.filter(task_id=task_id)
    students=[{ "id":task.student_id.id,"name":task.student_id.name } for task in tasks]
    print(students)
    students_ids=[task.student_id.id for task in tasks]
    add_students=CustomUser.objects.filter(role="Student").exclude(id__in=students_ids)
    task_name=Task.objects.get(task_id=task_id).task_name
    return render(request,'taskAssignment.html',{"students":students,"add_students":add_students,"task_id":task_name})

@login_required(redirect_field_name='/login/')
def deleteTask(request,pk,task_id):
    if(request.user.id!=pk or request.user.role!='Teacher'):
        return HttpResponse('Unauthorized', status=401)

    Task.objects.get(task_id=task_id).delete()
    return redirect(f'/teacher/dashboard/{pk}/')

@login_required(redirect_field_name='/login/')
def addStudentToTask(request,pk,task_id):
    if(request.user.id!=pk or request.user.role!='Teacher'):
        return HttpResponse('Unauthorized', status=401)
    if request.method=="POST":
        print(request.POST["student_id"])
        c=CustomUser.objects.get(id=request.POST["student_id"])
        assignment=TaskAssignment(student_id=c,task_id=Task.objects.get(task_id=task_id))
        assignment.save()
    return redirect(f'/teacher/dashboard/{pk}/view_task/{task_id}/')