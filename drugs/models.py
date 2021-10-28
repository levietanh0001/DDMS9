from django.db import models
from .drug_types import drug_types_list


class Drug(models.Model):
    drug_id = models.CharField(max_length=20, unique=True, error_messages={'unique':"This drug id has already been registered."})
    name = models.CharField(max_length=50)
    drug_type = models.CharField(max_length=20, choices=drug_types_list, default='pills', blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)
    exp = models.DateField(blank=True, null=True)
    mfg = models.DateField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True) 
    updated_date = models.DateField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name
