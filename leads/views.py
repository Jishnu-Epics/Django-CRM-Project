from django.core.mail import send_mail
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic 
from agents.mixins import OrganisorAndLoginRequiredMixin
from . models import Lead
from . forms import LeadForm,LeadModelForm,CustomUserCreationForm,AssignAgentForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")



class HomePageView(generic.TemplateView):
    template_name = "home.html"



def home_page(request):
    return render(request,"home.html")

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name="leads"
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                agent__isnull=False
                )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation,
                agent__isnull=False
                )
            queryset = queryset.filter(agent_user=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                agent__isnull=True
                )
        context.update({
            "unassigned_leads": queryset
             })
        return context

def lead_list(request):
    leads = Lead.objects.all( )
    context = {
        "leads":leads,
        
    }
    return render(request, "leads/lead_list.html",context)

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name="lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.UserProfile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent_user=user)
        return queryset




def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }
    
    return render(request, "leads/lead_detail.html",context)


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")


    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="jishnuvv23@gmail.com",
            recipient_list=["jishnuvv2016@gmail.com"]
        )
    
        return super(LeadCreateView, self).form_valid(form)
    




def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect("/leads")
    context = { 
        "form": form
        }
    return render(request,"leads/lead_create.html",context)


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.UserProfile)
    
    def get_success_url(self):
        return reverse("leads:lead-list")



def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
    
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
         }
    
    return render(request, "leads/lead_update.html",context)  


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    
    def get_success_url(self):
        return reverse("leads:lead-list")


    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.UserProfile)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")         


class AssignAgentView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_success_url(self):
        return reverse("leads:lead-list")

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

