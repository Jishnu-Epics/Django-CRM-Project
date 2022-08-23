from calendar import leapdays
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from . models import Lead


def leads_list(request):
    leads = Lead.objects.all( )
    context = {
        "leads":leads,
        
    }
    return render(request, "leads/lead_list.html",context)

def lead_details(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }
    
    return render(request, "leads/lead_detail.html",context)

def lead_create(request):
    return render(request,"leads/lead_create.html")