from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import job
from django.views.generic.base import TemplateView

def home(request):
    return render(request,'job_app/index.html',{})

def about(request):
    return render(request,'job_app/site/about.html',{})

def career_advice(request):
    return render(request,'job_app/site/career_advice.html',{})

def contact(request):
    return render(request,'job_app/site/contact.html',{})

def education(request):
    return render(request,'job_app/site/education.html',{})

def legal(request):
    return render(request,'job_app/site/legal.html',{})

def payroll(request):
    return render(request,'job_app/site/payroll.html',{})

def post_job(request):
    return render(request,'job_app/site/post_job.html',{})

def recruitment(request):
    return render(request,'job_app/site/recruitment.html',{})

def submit_resume(request):
    return render(request,'job_app/site/submit_resume.html',{})

class jobDetailView(DetailView):
    model = job
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['job']=job.objects.all()
        return context

class jobListView(ListView):
    model = job

'''
class IndexView(TemplateView):
    template_name="job_app/index.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['job']=job.objects.all()
        return context
'''

