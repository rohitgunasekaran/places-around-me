from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"index.html")

def vkids(request):
    return render(request,"vkids.html")

def primary(request):
    return render(request,"primary.html")

def middileclass(request):
    return render(request,"middileclass.html")

def ground(request):
    return render(request,"ground.html")

def highschool(request):
    return render(request,"highschool.html")

def highsecondary(request):
    return render(request,"highsecondary.html")