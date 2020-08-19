from django.shortcuts import render, redirect
from .models import Personal
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
# Create your views here.
def personal(request):
    username1=request.session['username']
    print(username1) 
    val=User.objects.filter(username=username1)
    for user in val:
        id1=user.id
    request.session['id']=id1
    trial=Personal.objects.filter(id=id1)
    if  trial.exists():
        print('not none')
        return redirect('documents')
    else:
        if request.method =="POST" :
            if  request.POST.get('dob') and request.POST.get('father') and request.POST.get('mother') and request.POST.get('phone') and request.POST.get('emergency') and request.POST.get('adr1') and request.POST.get('adr2') and request.POST.get('flatno') and request.POST.get('flatname') and request.POST.get('landmark') and request.POST.get('pincode'):
                print('personal none')
                post = Personal()
                post.id=id1
                post.date_of_birth = request.POST.get('dob')
                post.father_name = request.POST.get('father')
                post.mother_name = request.POST.get('mother')
                post.phone = request.POST.get('phone')
                post.ephone = request.POST.get('emergency')
                post.address1 = request.POST.get('adr1')
                post.address2 = request.POST.get('adr2')
                post.flat_number = request.POST.get('flatno')
                post.flat_name = request.POST.get('flatname')
                post.landmark = request.POST.get('landmark')
                post.pincode = request.POST.get('pincode')
                post.save()
                return redirect('documents')
        else:
            return render(request,'personal.html')
        
def logout(request):
    logout(request)
    return redirect('signin')