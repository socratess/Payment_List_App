from django.shortcuts import render, HttpResponse
from django.views import View, generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
# Create your views here.


class UserInformationView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name= 'account_settings/accountInformation.html'
    
    
    def get(self,request):
        userInformations =User.objects.get(username=request.user)
        context = {
            'userInformations': userInformations
        }
        return render(request,self.template_name, context)
    
    
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'account_settings/user_form.html'
    success_url = reverse_lazy('account_settings:UserInformation_all')
    
    #def get(self, request,pk):
    #    pass
    

class UserInactiveView (LoginRequiredMixin, UpdateView):
    model = User
    fields = ['is_active']
    template_name = 'account_settings/user_form.html'
    success_url = reverse_lazy('home:home_all')

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'account_settings/user_confirm_delete.html'
    