from django import forms
from django.forms import ModelForm, fields
from django.forms.models import ALL_FIELDS

from drugs.models import Drug
from .drug_types import drug_types_list

 
class DrugForm(forms.ModelForm):  
    class Meta:  
        model = Drug  
        fields = [
            'drug_id', 'name', 'drug_type',
            'amount', 'exp', 'mfg',
            'brand', 'description',
        ] 
        widgets = { 
            'drug_id': forms.TextInput(attrs={ 'class': 'form-control', 'data-val': 'true', 'data-val-required': 'Please enter drug id', }), 
            'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'drug_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'exp': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }), 
            'mfg': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }), 
            'brand': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'description': forms.TextInput(attrs={ 'class': 'form-control' }), 
            # 'updated_date': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }), 
        }
# from .models import Season, Drop, Product, Order, Delivery
# class DrugForm(forms.Form):
#     drug_id = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'drug_id',
#         'data-val': 'true',
#         'data-val-required': 'Please enter drug id',
#     }))
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     drug_type = forms.ChoiceField(widget=forms.Select(attrs={
#         'class': 'form-control',
#         'id': 'drug_type',
#         # 'data-val': 'true',
#         # 'data-val-required': 'Please enter drug type',
#     }), choices=drug_types_list)
#     amount = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'amount',
#         # 'data-val': 'true',
#         # 'data-val-required': 'Please enter amount',
#     }), required=False)
#     exp = forms.CharField(widget=forms.DateInput(attrs={
#         'class': 'form-control',
#         'type': 'date',
#         'id': 'exp',
#         # 'data-val': 'true',
#         # 'data-val-required': 'Please enter expiry date',
#     }), required=False)
#     mfg = forms.CharField(widget=forms.DateInput(attrs={
#         'class': 'form-control',
#         'type': 'date',
#         'id': 'exp',
#         # 'data-val': 'true',
#         # 'data-val-required': 'Please enter manufacture date',
#     }), required=False)
#     brand = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'brand',
#         # 'data-val': 'true',
#         # 'data-val-required': 'Please enter brand',
#     }), required=False)
#     description = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'description',
#         # 'data-val': 'true',
#         # 'data-val-required': 'Please enter description',
#     }), required=False)
#     updated_date = forms.CharField(widget=forms.DateInput(attrs={
#         'class': 'form-control',
#         'type': 'date',
#         'id': 'updated_date',
#         # 'data-val': 'true',
#         # 'data-val-required': 'Please enter updated date',
#     }), required=False)

