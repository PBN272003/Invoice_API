from django.contrib import admin
from .models import Invoice, InvoiceDetail
# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'invoice_no', 'customer_name')

@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('id','invoice', 'description', 'quantity', 'unit_price', 'price')