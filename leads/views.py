from calendar import leapdays
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from . models import Lead


def leads_list(request):
    leads = Lead.objects.all( )
    context = {
        
    }
    return render(request, "home.html",context)

