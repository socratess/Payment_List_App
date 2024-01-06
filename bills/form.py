from django import forms
from bills.models import Bill, BankEntity

class CreateBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['title', 'description', 'price', 'important']
    
class CreateBankEntityForm(forms.ModelForm):
    class Meta:
        model = BankEntity
        fields = ['name','frequent']
        
        

class UpdatePaymentBillForm(forms.ModelForm):
    title = forms.CharField(disabled=True)
    description = forms.CharField(disabled=True)
    price = forms.FloatField(disabled=True)
    class Meta:
        model= Bill
        fields = ['title', 'description', 'price']
                
        