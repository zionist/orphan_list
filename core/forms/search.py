# -*- coding:utf-8 -*-

from django import forms
from core.models.passport import Passport
from common.constants import DEFAULT_SEARCH_TRUE_VALUES

class SearchForm(forms.ModelForm):
    class Meta:
       model = Passport

class QuickSearchForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=255, required=False)
    surname = forms.CharField(label="Фамилия", max_length=255, 
        required=False)
    birthday = forms.DateField(label="Дата рождения", required=False)

# dynamic search forms
class SearchForm(forms.Form):
    def __init__(self, form_data=None, *args, **kwargs):
        """
        :param form_data: dict {fields name: label} for dynamic form generation
        :return: search form with fields according input form_data dict
        """
        super(SearchForm, self).__init__(*args, **kwargs)
        passport_field_names = [field.name for field in Passport._meta.fields if field.name != "id"]
        if form_data:
            for k, v in form_data.items():
                # only for field names which are in Passport model
                if k in passport_field_names:
                    self.fields[k] = forms.CharField(required=False, label=v)

class SearchSelectForm(forms.Form):
    from_yeah = forms.BooleanField(label="Начиная с года рождения", required=False)
    to_yeah = forms.BooleanField(label="Заканчивая годом рождения", required=False)
    age = forms.BooleanField(label="Возраст", initial=True, required=False)

    def __init__(self, *args, **kwargs):
        """
        :return: form for select search fields
        """
        super(SearchSelectForm, self).__init__(*args, **kwargs)
        form_fields = [{field.name: field.help_text} for field in Passport._meta.fields if field.name != "id"]
        for field in form_fields:
            name = field.keys()[0]
            help_text = field.values()[0]
            if name in DEFAULT_SEARCH_TRUE_VALUES:
                self.fields[name] = forms.BooleanField(required=False, label=help_text, initial=True)
            else:
                self.fields[name] = forms.BooleanField(required=False, label=help_text)
