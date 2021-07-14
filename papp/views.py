from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def education(request):
    return render(request, 'education.html')