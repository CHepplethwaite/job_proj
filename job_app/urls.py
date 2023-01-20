from django.urls import path
from . import views as job_views

urlpatterns =[
    path('',job_views.home,name='home')
]