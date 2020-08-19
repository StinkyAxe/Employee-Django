from django.shortcuts import render, redirect
from .models import Documents
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout

# Create your views here.
def documents(request):
    id1=request.session['id']   
    trial=Documents.objects.filter(id=id1)
    print("doc",id1)
    if trial.exists():
        print('doc not none')
        return redirect('extraactivity')

    else:
        if request.method == 'POST':
            if request.POST.get('tenroll') and request.POST.get('tenboard') or request.POST.get('tenschool') and request.POST.get('tenpercent') and request.POST.get('twelveroll') and request.POST.get('twelveboard') and request.POST.get('twelveschool') and request.POST.get('twelvepercent') and request.POST.get('degree') and request.POST.get('university') and request.POST.get('college') and request.POST.get('roll') and request.POST.get('percent'):
                print('doc none')
                post = Documents()
                post.id=id1
                post.roll_x = request.POST.get('tenroll')
                post.board_x = request.POST.get('tenboard')
                post.school_x= request.POST.get('tenschool')
                post.percentage_x = request.POST.get('tenpercent')
                post.roll_xii = request.POST.get('twelveroll')
                post.board_xii = request.POST.get('twelveboard')
                post.school_xii = request.POST.get('twelveschool')
                post.percentage_xii = request.POST.get('twelvepercent')
                post.degree_name = request.POST.get('degree')
                post.univ_name = request.POST.get('university')
                post.college_name = request.POST.get('college')
                post.univ_roll = request.POST.get('roll')
                post.percentage= request.POST.get('percent')
                post.save()
                return redirect('extraactivity')
        else:
            return render(request,'documents.html')
def logout(request):
    logout(request)
    return redirect('signin')