from django.urls import path
from . views import  leads_list,lead_details    

app_name = "leads"

urlpatterns = [
    
    path('',leads_list),
    path('<pk>/',lead_details)
]