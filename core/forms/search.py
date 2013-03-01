# -*- coding:utf-8 -*-

from django import forms
from core.models.passport import Passport


class SearchForm(forms.ModelForm):
    class Meta:
       model = Passport

class QuickSearchForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=255, required=False)
    surname = forms.CharField(label="Фамилия", max_length=255, 
        required=False)
    birthday = forms.DateField(label="Дата рождения", required=False)
