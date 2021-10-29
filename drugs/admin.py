from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# local
from .models import Drug
from .forms import DrugForm

    
class DrugAdmin(ImportExportModelAdmin):
    fields = ('drug_type',)
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
    form = DrugForm
    list_per_page = 20
    search_fields = ['drug_id', 'name', 'drug_type', 'brand', 'description']
admin.site.register(Drug, DrugAdmin)






# autocomplete search
    # https://stackoverflow.com/questions/50960800/searchable-drop-down-for-choice-field-in-django-admin
    
