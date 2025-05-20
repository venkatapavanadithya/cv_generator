from django.http import HttpResponse
from django.shortcuts import render
from app.models import Profile
import pdfkit
from django.template import loader

# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        about=request.POST.get("about")
        degree=request.POST.get("degree")
        university=request.POST.get("university")
        school=request.POST.get("school")
        previous_work=request.POST.get("previous_work")
        skills=request.POST.get("skills")
        profile=Profile(name=name,email=email,summary=about,university=university,school=school,degree=degree,previous_work=previous_work,skills=skills,phone=phone)
        profile.save()
    return render(request,'app/accept.html')
def resume(request,id):
    user_profile=Profile.objects.get(id=id)
    template=loader.get_template('app/resume.html')
    html=template.render({'user_profile':user_profile})
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
    }
    pdf=pdfkit.from_string(html,False,options=options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachement;filename="resume.pdf"'
    return response

def list(request):
    profiles=Profile.objects.all()
    return render(request,'app/list.html',{'profiles':profiles})