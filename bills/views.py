from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Bill, BankEntity
from django.views.generic.edit import CreateView, UpdateView
from bills.form import CreateBillForm, CreateBankEntityForm, UpdatePaymentBillForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.serializers import serialize
import json
from django.views.generic import TemplateView
# Create your views here.


class BillListView(LoginRequiredMixin,generic.ListView):
           
    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)

    
    def get(self, request, *args, **kwargs):
        serialized_data = (serialize("json", self.get_queryset(), use_natural_foreign_keys=True))
        return JsonResponse(json.loads(serialized_data),safe=False, status=200)
      
class BankListView(LoginRequiredMixin,generic.ListView): 
    
    def get_queryset(self):
        return BankEntity.objects.filter(bill__in=list(Bill.objects.filter(user=self.request.user).values_list('id')))
    
    def get(self, request, *args, **kwargs):
        serialized_data_bank = (
            serialize("json", self.get_queryset(), use_natural_foreign_keys=True))
        
        print(serialized_data_bank)
        
        return JsonResponse(json.loads(serialized_data_bank), safe=False, status=200)
    

class BillCreateView(LoginRequiredMixin,CreateView):
    template_name = 'bills/bill_form.html'
    success_url = reverse_lazy("bills:all")
   
    def get(self, request, pk=None):
        formBill = CreateBillForm()
        formBank = CreateBankEntityForm()
        
        ctx = {'formBill': formBill, 'formBank': formBank}
        return render(request, self.template_name, ctx)
    
    def post(self,request,pk=None):
        formBill = CreateBillForm(request.POST, request.FILES or None)
        formBank = CreateBankEntityForm(request.POST, request.FILES or None)
        
        if not (formBill.is_valid()):
            message = 'Bill and Bank are not saved successfully!'
            error = formBill.errors
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 400
            return response
            #ctx = {'formBill': formBill, 'formBank': formBank}
            #return render(request,self.template_name, ctx)
        if not (formBank.is_valid()):
            message = 'Bill and Bank are not saved successfully!'
            error = formBank.errors
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 400
            return response
        
        
        
        
        bill = formBill.save(commit=False)
        bill.user = request.user
        bill.save()
        banks = formBank.save(commit=False)
        banks.bill = bill
        banks.save()
        message = 'Bill and Bank saved successfully!'
        error='there is not error'
        response = JsonResponse({'message':message,'error':error})
        response.status_code=201
        return response
 #      return redirect(self.success_url)
     
class BillDetailView(LoginRequiredMixin,generic.DetailView):
    model = Bill
    template_name = 'bills/bill_detail.html'

    def get(self, request, pk):
        x = Bill.objects.get(id=pk)
        try:
            banks = BankEntity.objects.get(bill=x)
            context = {'bill':x,'banks': banks}
            return JsonResponse(request, self.template_name, context)
        except:
            context = {'bill': x}
            return render(request, self.template_name, context)
        

class BankDetailView(LoginRequiredMixin, generic.DetailView):
    model= BankEntity
    template_name = 'banks/bank_detail.html'
    
    def get(self, request, pk):
        x =  BankEntity.objects.get(id=pk)
        print(x.bill)
        #try:
        #    banks = Bill.objects.get(id=x.bill)
        #    context = {'bill': x, 'banks': banks}
        #    return render(request, self.template_name, context)
        #except:
        context = {'bank': x}
        return render(request, self.template_name, context)
              
class BillUpdateView(LoginRequiredMixin,UpdateView):
    model = Bill
    fields = ['title', 'description', 'price', 'important']
    template_name = 'bills/bill_form_update.html'
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        formBill = CreateBillForm(request.POST, instance=self.get_object())

        if not (formBill.is_valid()):
            message = 'Bill is not updated successfully!'
            error = formBill.errors
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 400
            return response

        formBill.save()
        message = 'Bill updated successfully!'
        error = 'there is not error'
        response = JsonResponse({'message': message, 'error': error})
        response.status_code = 201
        return response

    
    
class BillDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Bill
    template_name = 'bills/bill_delete.html' 
    
    def delete(self, request, *args, **kwargs):
        bill = self.get_object()
        bill.delete()
        message = 'Bill deleted successfully!'
        error = 'there is not error'
        response = JsonResponse({'message': message, 'error': error})
        response.status_code = 201
        return response

class BankEntityUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = BankEntity
    fields = ['name', 'frequent']
    template_name = 'banks/bank_form_update.html'
    success_url = reverse_lazy('bills:bankall')
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        formBank = CreateBankEntityForm(request.POST, instance=self.get_object())

        if not (formBank.is_valid()):
            message = 'Bank is not updated successfully!'
            error = formBank.errors
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 400
            return response

        
        formBank.save()
        message = 'Bank updated successfully!'
        error = 'there is not error'
        response = JsonResponse({'message': message, 'error': error})
        response.status_code = 201
        return response
    
class BillPaidView(LoginRequiredMixin, generic.ListView):
    
    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user, datecompleted__isnull=False).order_by('-datecompleted')

    def get(self, request, *args, **kwargs):
        serialized_data = (
            serialize("json", self.get_queryset(), use_natural_foreign_keys=True))
        return JsonResponse(json.loads(serialized_data), safe=False, status=200)

class BillUnpaidView(LoginRequiredMixin,generic.ListView):
    
    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user, datecompleted__isnull=True).order_by('-datecompleted')

    def get(self, request, *args, **kwargs):
        serialized_data = (
            serialize("json", self.get_queryset(), use_natural_foreign_keys=True))
        return JsonResponse(json.loads(serialized_data), safe=False, status=200)

'''@login_required
def bill_pay(request, bill_id):
    bills = get_object_or_404(Bill, pk=bill_id, user=request.user)
    success_url = reverse_lazy('bills:bill_unpaid')
    if request.method == 'POST':
        bills.datecompleted = timezone.now()
        bills.save()
        messages.success(request, "Paid successful.")
        return redirect(success_url)
    messages.error(request, "Paid failed.")
'''

class BillPayBill(LoginRequiredMixin, generic.UpdateView):
     model = Bill   
     template_name = 'bills/bill_payment.html'
     form_class = UpdatePaymentBillForm

     def post(self, request, *args, **kwargs):
        formBill = UpdatePaymentBillForm(request.POST, instance=self.get_object())

        if not (formBill.is_valid()):
            message = 'Bill is not payed successfully!'
            error = formBill.errors
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 400
            return response

        bill = formBill.save(commit=False)
        bill.datecompleted = timezone.now()
        bill.save() 
        message = 'Bill payed successfully!'
        error = 'there is not error'
        response = JsonResponse({'message': message, 'error': error})
        response.status_code = 201
        return response
   
              

@login_required
def UploadManualBillView(request):
    #success_url = reverse_lazy('bills:all')
    try: 
        if request.method == 'POST' and request.FILES['myfile']:
            dbframe = pd.read_excel(FileSystemStorage().save(
                request.FILES['myfile'].name, request.FILES['myfile']))
            for dbframe in dbframe.itertuples():
                billObj = Bill.objects.create(
                    title=dbframe.title, 
                    description=dbframe.description, 
                    price=dbframe.price,
                    user=request.user
                )
                billObj.save()         
                bankObj=BankEntity.objects.create(
                    name=dbframe.name,
                    bill=billObj          
                )
                bankObj.save()
                
            message = 'Bill and Bank uploaded successfully!'
            response = JsonResponse({'message':message})
            response.status_code=201
            return response       
            #return redirect(success_url)
        else:
            message = 'Bill and Bank are not upload successfully!'
            response = JsonResponse({'message': message})
            response.status_code = 400
            return response
            #return render(request, 'manual_bill/upload_bill.html')    
    except:
        message = 'Bill and Bank are not uploaded successfully!'
        response = JsonResponse({'message': message})
        response.status_code = 400
        return response
