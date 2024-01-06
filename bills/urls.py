from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = 'bills'

urlpatterns = [
    path("", views.BillListView.as_view(), name="all"),
    path("<int:pk>", views.BillDetailView.as_view(), name="bill_detail"),
    path("create", views.BillCreateView.as_view(), name="bill_create"),
    path("<int:pk>/update", views.BillUpdateView.as_view(success_url=reverse_lazy('bills:all')), name="bill_update"),
    path("<int:pk>/delete", views.BillDeleteView.as_view(success_url=reverse_lazy("bills:all")), name="bill_delete"),
    path("bank/", views.BankListView.as_view(), name="bankall"),
    path("bank/<int:pk>/update",views.BankEntityUpdateView.as_view(), name="banks_update"),
    path("bank/<int:pk>", views.BankDetailView.as_view(), name="bank_detail"),
    path("paid", views.BillPaidView.as_view(), name="bill_paid"),
    path("unpaid", views.BillUnpaidView.as_view(), name="bill_unpaid"),
    path("<int:pk>/pay", views.BillPayBill.as_view(), name="bill_pay"),
    path("manualupload/", views.UploadManualBillView, name="manualbill_all"),
]

urlpatterns +=[
    path('startbill/', login_required(TemplateView.as_view(template_name="bills/bill_list.html")), name='start_bill'),
    path("startbank/",login_required(TemplateView.as_view(template_name="banks/bank_list.html")), name="start_bankall"),
    path("billupload/",login_required(TemplateView.as_view(template_name="manual_bill/manual_bill_upload.html")), name="bill_upload"),
    path('startbillpaid/', login_required(TemplateView.as_view(template_name="bills/bill_paid_list.html")), name='start_billpaid'),
    path('startbillunpaid/', login_required(TemplateView.as_view(template_name="bills/bill_unpaid_list.html")), name='start_billunpaid'),
    ]