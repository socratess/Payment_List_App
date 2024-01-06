from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AboutView(LoginRequiredMixin,View):
    def get(self,request):
        #print('host: ',request.get_host())
        #host = request.get_host()
        #islocal = host.find('localhost') >=0 or host.find('127.0.0.1') >=0
        context = {
            'installed': settings.INSTALLED_APPS, 
        #    'islocal':islocal
        }
        return render(request, 'about/about.html',context)