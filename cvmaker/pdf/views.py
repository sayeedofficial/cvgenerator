from django.shortcuts import render
from .models import Profile

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name","");
        email = request.POST.get("email","");
        phone = request.POST.get("phone","");
        summary = request.POST.get("summary","");
        degree = request.POST.get("degree","");
        school = request.POST.get("school","");
        university = request.POST.get("university","");
        previouswork = request.POST.get("previouswork","");
        skills = request.POST.get("skills","");
        
        profile = Profile(name=name,email=email,phone=phone,summary = summary,degree=degree,school=school,university=university,previouswork=previouswork,skills=skills)
        profile.save()








    return render(request, "pdf/index.html")

