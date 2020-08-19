from django.shortcuts import render, redirect
from io import BytesIO
from django.http import HttpResponse, request
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa
from django.contrib.auth.models import User
from personal.models import Personal
from documents.models import Documents
from extraactivity.models import Extraactivity
from uploaddocuments.models import Uploaddocuments
import employee
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
#from .utils import render_to_pdf
import datetime
from .utils import render_to_pdf
#from employee import extraactivity
# Create your views here.  
def landingpage(request):
    if request.method == "POST":
        id1=request.session['id']
        users=User.objects.filter(id=id1)
        for u in users: #for name and email:
            email1 = u.email
            username = u.first_name
        personals = Personal.objects.filter(id=id1) #personal page
        for p in personals:
            borndate = p.date_of_birth
            father = p.father_name
            mother = p.mother_name
            mobile = p.phone
            emergency = p.ephone
            address_1 = p.address1
            address_2 = p.address2
            flat_no = p.flat_number
            flat_name = p.flat_name
            land_mark = p.landmark
            pin_code = p.pincode
        documentx = Documents.objects.filter(id=id1) #document page
        for d in documentx:
            roll1 = d.roll_x
            board1 = d.board_x
            school1 = d.school_x
            percentage1 = d.percentage_x
            roll2= d.roll_xii
            board2= d.board_xii
            school2 = d.school_xii
            percentage2 = d.percentage_xii
            degree = d.degree_name
            university = d.univ_name
            roll3 = d.univ_roll
            college = d.college_name
            percentage = d.percentage    
        extraactivityx = Extraactivity.objects.filter(id=id1) #extraactivity page
        for e in extraactivityx:
            ten1 = e.ten_details
            twelve1 = e.twelve_details
            grad1 = e.graduation_details
        upload = Uploaddocuments.objects.filter(id=id1) #uploaded picture
        for u in upload:
            pic = u.photo
        
        template = get_template('pdf.html')
           
        data = {
            'today': datetime.date.today(),
            'email': email1,
            'name': username,
            'dob': borndate,
            'fname': father,
            'mname': mother,
            'phone': mobile,
            'emergency': emergency,
            'address1': address_1,
            'address2': address_2,
            'flatno' : flat_no,
            'flatname': flat_name,
            'landmark': land_mark,
            'pincode': pin_code,
            'roll_10': roll1,
            'board10': board1,
            'school10': school1,
            'percentage10': percentage1,
            'roll_12': roll2,
            'board12': board2,
            'school12': school2,
            'percentage12': percentage2,
            'degree': degree,
            'university': university,
            'univ_roll': roll3,
            'college': college,
            'percentage': percentage,
            'eten': ten1,
            'etwelve': twelve1,
            'egrad': grad1,
            'photo1':pic
        }
        
         
        html = template.render(data)
        pdf = render_to_pdf('pdf.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Declaration_%s.pdf" %("Declaration1234")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
    else:
        return render(request,'landingpage.html')

def logout(request):
    logout(request)
    return redirect('signin')


