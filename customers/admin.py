from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'cpf', 'phone')
    ordering = ('name',)
