from django.shortcuts import render, redirect
from .models import Extraactivity
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout

# Create your views here.
def extraactivity(request):
    id1=request.session['id']
    trial=Extraactivity.objects.filter(id=id1)
    print("extra",id1)
    if trial.exists():
        return redirect('uploaddocuments')
    else:
        if request.method == 'POST':
            if request.POST.get('ten') and request.POST.get('twelve') and request.POST.get('graduation'):
                post = Extraactivity()
                post.id=id1
                post.ten_details = request.POST.get('ten')
                post.twelve_details = request.POST.get('twelve')
                post.graduation_details= request.POST.get('graduation')
                post.save()
                return redirect('uploaddocuments')
        else:
            return render(request,'extraactivity.html')
def logout(request):
    logout(request)
    return redirect('signin')