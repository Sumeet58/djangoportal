from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import TemplateView 

# Create your views here.
class HomePageView(TemplateView): 
     def get(self, request, **kwargs): 
 	 
         return render(request, 'index.html', context=None) 

class login(TemplateView): 
     def get(self, request, **kwargs): 
          
         return render(request, 'login.html', context=None) 

class reg(TemplateView): 
     def get(self, request, **kwargs): 
          
         return render(request, 'reg.html', context=None) 
