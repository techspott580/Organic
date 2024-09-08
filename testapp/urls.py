from django.contrib import admin
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('',views.index,name='Home'), 
    path('about',views.about,name='About'), 
    path('services',views.services,name='services'), 
    path('contact',views.contact,name='contact'), 
    path('Organic_Farming',views.Organic_Farming,name='Organic_Farming'), 
    path('Organic_Fruits',views.Organic_Fruits,name='Organic_Fruits'), 
    path('Organization_Information',views.Organization_Information,name='Organization_Information'), 
]