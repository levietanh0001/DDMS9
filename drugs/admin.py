from django.contrib import admin
from .models import Drug


class DrugAdmin(admin.ModelAdmin):
    list_display = [
        'drug_id',
        'name',
        'drug_type',
        'amount',
        'exp',
        'mfg',
        'brand',
        'description',
        'updated_date',
    ]
    
    
admin.site.register(Drug, DrugAdmin)