from django.urls import path
from . views import  lead_create, lead_update, leads_list,lead_details    

app_name = "leads"

urlpatterns = [
    
    path('',leads_list),
    path('<int:pk>/',lead_details),
    path('<int:pk>/update/',lead_update),
    path('create',lead_create),
]