from django.shortcuts import render,redirect
from . models import Lead
from . forms import LeadModelForm


def lead_list(request):
    leads = Lead.objects.all( )
    context = {
        "leads":leads,
        
    }
    return render(request, "leads/lead_list.html",context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }
    
    return render(request, "leads/lead_detail.html",context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect("/leads")
    context = { 
        "forms":LeadModelForm()
        }
    return render(request,"leads/lead_create.html",context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
    
            return redirect("/leads")
    context = {
        "forms":LeadModelForm(),
        "lead": lead
         }
    
    return render(request, "leads/lead_update.html",context)  




def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")         


# def lead_update(request,pk):
#      lead = Lead.objects.get(id=pk)
#      form = LeadForm()
#      if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
    
#             return redirect("/leads")
    #  context = {
    #     "forms":LeadModelForm(),
    #     "lead": lead
    #      }
    
    #  return render(request, "leads/lead_update.html",context)





# def lead_create(request):
    # form = LeadForm()
    # if request.method == "POST":
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = form.cleaned_data['agent']
            
    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent

    #         )
    
    #         return redirect("/leads")
#     context = { 
#         "forms":LeadForm()
#         }
#     return render(request,"leads/lead_create.html",context)

