from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import todo as TodoModel
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(requests):
    return render(requests,'home.html')

def login_(requests):
    if requests.POST:
        usn=requests.POST.get('username')
        pas=requests.POST.get('password')
        user=authenticate(requests,username=usn, password=pas)
        if  user is not None:
            login(requests,user)
            return redirect('todo')
        else:
            return render(requests,'login.html',{'error':'Username/password is wrong'})
    return render(requests,'login.html')


def signup(requests):
    if requests.POST:
        usrname=requests.POST.get('username')
        password=requests.POST.get('password')
        email=requests.POST.get('email')
        if usrname=='' or password==''or email=='':
            return render(requests,'signup.html',{'error': 'Please fill all fields'})
        if User.objects.filter(username=usrname).exists():
            return render(requests,'signup.html',{'error': 'username already exists'})        
        if User.objects.filter(email=email).exists():
            return render(requests,'signup.html',{'error': 'email already registred'})        
        usr=User.objects.create_user(usrname,email,password)
        usr.save()
        return redirect('/login')
    return render(requests,'signup.html')
    
@login_required(login_url='login')
def todo(requests):
    if requests.POST:
        task=requests.POST.get('task')
        if task:
            obj=TodoModel(title=task,user=requests.user)
            obj.save()
            return redirect('todo')
    tasks=TodoModel.objects.filter(user=requests.user).order_by('-date')
    return render(requests,'todo.html',{"tasks":tasks})


@login_required(login_url='login')
def edit(requests,srno):
    task=TodoModel.objects.get(user=requests.user,srno=srno)
    if requests.POST:
        edit_task=requests.POST.get('edit')
        if task:
            task.title=edit_task
            task.save()
            return redirect('todo')

    return render(requests,'edit.html',{'task':task})

@login_required(login_url='login')
def delete(requests,srno):
    task=TodoModel.objects.get(user=requests.user,srno=srno)
    task.delete()
    return redirect('todo')
    
def logout_(requests):
    logout(requests)
    return redirect('login')


