from django.contrib import admin
from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.urls import path
from django.shortcuts import render, redirect
from django import forms
# local
from .models import Drug

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
    
    
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
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return my_urls + urls
    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Only CSV files are accepted!')
                return HttpResponseRedirect(request.path_info)
            
            
            f = csv_file.read().decode('utf-8')
            csv_data = f.split("\n")
            for x in csv_data:
                fields = x.split(",")
                created = Drug.objects.update_or_create(
                    drug_id = fields[0],
                    name = fields[1],
                    drug_type = fields[2],
                    amount = fields[3],
                    exp = fields[4],
                    mfg = fields[5],
                    brand = fields[6],
                    description = fields[7],
                    updated_date = fields[8],
                )
            self.message_user(request, "Your csv file has been uploaded!")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_upload.html", payload)
    
admin.site.register(Drug, DrugAdmin)