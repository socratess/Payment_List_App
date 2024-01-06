from django.contrib import admin
from .models import Bill, BankEntity

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = BankEntity
    extra = 1


class BillAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ("title", "price", "user", "created", "important")
    fieldsets = [
        ("Main Information", {"fields": ["title", "description", "price"]}),
        ("Priority Information", {"fields": ["important"], "classes":['collapse']}),
        ("User Information", {"fields": ["user"], "classes":["collapse"]}),
        ("Date Information", {"fields": [
         "datecompleted", "created"], "classes":['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_filter = ["created"]
    search_fields=["title","price"]

#class BankEntityAdmin(admin.ModelAdmin):
#    readonly_fields = ("created",)
#    list_display = ("name", "bill", "created")
    

admin.site.register(Bill,BillAdmin)
#admin.site.register(BankEntity, BankEntityAdmin)
