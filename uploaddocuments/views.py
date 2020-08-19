from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Uploaddocuments
from django.contrib.auth import logout

# Create your views here.
def uploaddocuments(request):
    id1=request.session['id']   
    trial=Uploaddocuments.objects.filter(id=id1)
    print("doc",id1)
    if trial.exists():
        print('doc not none')
        return redirect('landingpage')
    else:
        if request.method =='POST':
            post = Uploaddocuments()
            post.ten_x = request.FILES['ten']
            post.id = id1
            post.twelve_xii = request.FILES['twelve']
            post.graduate = request.FILES['graduation']
            post.photo = request.FILES['photo']
            fs = FileSystemStorage()
            post.save()
            return redirect('landingpage')
        else:   
            return render(request,'uploaddocuments.html')

def logout(request):
    logout(request)
    return redirect('signin')

            
