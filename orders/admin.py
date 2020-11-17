from django.contrib import admin
from .models import Order, Row


class RowInline(admin.TabularInline):
    model = Row


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        RowInline
    ]
    date_hierarchy = 'created'
    list_display = ('number', 'date', 'client', 'marketplace', 'status', 'eurozone', 'created', 'read', 'processed')


#admin.site.register(Order, OrderAdmin)
