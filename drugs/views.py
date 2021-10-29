from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import View

from datetime import datetime
from .models import (
    Drug,
)
from .forms import (
    DrugForm,
)
# Create your views here.
# Supplier views
# @login_required(login_url='login')
def add_drug(request):
    forms = DrugForm()
    if request.method == 'POST':
        forms = DrugForm(request.POST)
        if forms.is_valid():
            drug_id = forms.cleaned_data['drug_id']
            name = forms.cleaned_data['name']
            drug_type = forms.cleaned_data['drug_type']
            amount = forms.cleaned_data['amount']
            exp = forms.cleaned_data['exp']
            mfg = forms.cleaned_data['mfg']
            brand = forms.cleaned_data['brand']
            description = forms.cleaned_data['description']
            # updated_date = forms.cleaned_data['updated_date']
            Drug.objects.create(drug_id=drug_id, name=name, 
                drug_type=drug_type, amount=amount, exp=exp, mfg=mfg, brand=brand, description=description)
            return redirect('drug-list')
    context = {
        'form': forms
    }
    return render(request, 'drugs/add_drug.html', context)    



def delete_selected(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('instance')
        for i in id_list:
            Drug.objects.get(drug_id=i).delete()
            return redirect("drug-list")
def destroy(request, drug_id):  
    drug = get_object_or_404(Drug, drug_id=drug_id)
    drug.delete()
    return redirect("/")
def edit(request, drug_id):  
    drug = get_object_or_404(Drug, drug_id=drug_id)
    # forms = DrugForm()
    context = {
        'drug': drug
    }
    return render(request, 'drugs/edit_drug.html', context)
def update(request, drug_id):  
    # drug = Drug.objects.get(drug_id=drug_id)  
    # form = DrugForm(request.POST)  
    drug = get_object_or_404(Drug, drug_id=drug_id)
    form = DrugForm(request.POST, instance = drug)  
    # form = DrugForm(drug[0])
    if form.is_valid():  
        form.save()
        return redirect("drug-list") 
    return render(request, 'drugs/edit_drug.html', {'drug': drug}) 
    # drug_id = drug.drug_id
    # name = drug.name
    # drug_type = drug.drug_type
    # amount = drug.amount
    # exp = drug.exp
    # mfg = drug.mfg
    # brand = drug.brand
    # description = drug.description
    # updated_date = drug.updated_date
    # if exp == '':
    #     exp = None
    # if mfg == '':
    #     mfg = None
    # if updated_date == '':
    #     updated_date = None
    # Drug.objects.filter(drug_id=drug_id).update(drug_id=drug_id, name=name, 
    #     drug_type=drug_type, amount=amount, exp=exp, mfg=mfg, brand=brand, description=description, updated_date=updated_date)
         
    
class DrugListView(ListView):
    model = Drug
    template_name = 'drugs/drug_list.html'
    context_object_name = 'drug'
    
    
class DrugCatalogListView(ListView):
    model = Drug
    template_name = 'drugs/catalog.html'
    context_object_name = 'drug'    

    
# Create your views here.
def drug_image_view(request):
  
    if request.method == 'POST':
        form = DrugForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DrugForm()
    return render(request, 'upload_drug_img.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')    
