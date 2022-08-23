from django.urls import path
from . views import  lead_create, leads_list,lead_details    

app_name = "leads"

urlpatterns = [
    
    path('',leads_list),
    path('<int:pk>/',lead_details),
    path('create',lead_create),
]