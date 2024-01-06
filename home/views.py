from django.shortcuts import render
from django.views import View
from django.conf import settings
from random import random 
# Create your views here.


class HomeView(View):
        
    def get(self,request):
        #print('host: ',request.get_host())
        #host = request.get_host()
        #islocal = host.find('localhost') >=0 or host.find('127.0.0.1') >=0
        #num_visits = request.session.get('num_visits',0)+1
        #request.session['num_visits'] = num_visits
        #print(num_visits)
        #if num_visits > 8: del(request.session['num_visits'])
        context = {
            'installed': settings.INSTALLED_APPS,
            'user': request.user
        #    'islocal':islocal
        }
        response = render(request, 'home/main.html',context)
        response.set_cookie('payment', 12)
        response.set_cookie('payment_list',24,max_age=100)
        return response
