from django.shortcuts import render

def home(request):
    return render(request,'job_app/index.html',{})
