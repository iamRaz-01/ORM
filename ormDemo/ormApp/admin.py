from django.contrib import admin
from .models import Bank, Customer, Loan

class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'ifsc_code')  
    search_fields = ('name', 'branch', 'ifsc_code')  
    list_filter = ('branch',)  
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')  
    search_fields = ('first_name', 'last_name', 'email', 'phone')  
    list_filter = ('first_name',)  
    
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'customer', 'bank', 'loan_amount', 'status', 'date_applied')  
    search_fields = ('loan_id', 'customer__first_name', 'bank__name', 'status')  
    list_filter = ('status', 'bank', 'date_applied')  
    list_editable = ('status',)  
    
admin.site.register(Bank)
admin.site.register(Customer)
admin.site.register(Loan)
