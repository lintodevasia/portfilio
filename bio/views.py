from django.shortcuts import render
from .models import project
from . models import Experience
from .models import skill
from .models import profile




# Create your views here.
def home(request):
    obj= project.objects.all()
    obj1=Experience.objects.all()
    obj2=skill.objects.all()
    obj3=profile.objects.all()
    return render(request, "home.html", {'projects': obj,'exp':obj1,'skl':obj2,'dp':obj3})


