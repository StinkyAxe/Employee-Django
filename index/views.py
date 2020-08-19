from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['repassword']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                return HttpResponse('<br><h2 style="text-align:center;">Email exits.Please use different email..Press back button and try again..</h2>')
                return redirect('index')
            elif User.objects.filter(username=username).exists():
                return HttpResponse('<br><p style="text-align:center;">Username Already taken! Please use another username..Press back button and try again..</h2>')
                return redirect('index')
            else:
                user=User.objects.create_user(first_name=name,username=username,email=email,password=password1)
                user.save()
                return HttpResponse('<br><h2 style="text-align:center;">User successfully created! Please proceed to login by clicking the back button and click on signin :)</h2>')
                return redirect('signin')
        else:
            return HttpResponse('<br><h2 style="text-align:center;">Passwords not matching!! Press back button and try again.. :)</h2>')
            return redirect('index')
    else:
        return render(request,'index.html')

def signin(request):
    next = request.GET.get('next', '/admin')
    if request.method=="POST":
        username1=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username1,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['username'] = username1
                return redirect('personal')
            else:
                messages.info(request,'Inactive user')
        else:
            return HttpResponse('<br><h2 style="text-align:center;">Invalid UserID/Password..Press back button and try again with the correct userID and Password :)</h2>')
            return redirect('signin')    
    else:
        return render(request,'signin.html')  

def logout(request):
    logout(request)
    return redirect('signin')