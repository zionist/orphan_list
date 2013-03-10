# -*- coding:utf-8 -*-

from django import forms
from core.models.passport import Passport
from common.constants import DEFAULT_SEARCH_TRUE_VALUES, EXTRA_SEARCH_FIELDS
from django.utils.encoding import smart_text

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
    def __init__(self, generate_from=None, *args, **kwargs):
        """
        :param form_data: dict {fields name: label} for dynamic form generation
        :return: search form with fields according input form_data dict
        """
        if not generate_from:
            generate_from = DEFAULT_SEARCH_TRUE_VALUES
        super(SearchForm, self).__init__(*args, **kwargs)
        passport_field_names = [field.name for field in Passport._meta.fields if field.name != "id"]

        # convert to unicode
        for key, value in generate_from.items():
            generate_from[key] = smart_text(value)
        generate_from = sorted(generate_from.items(), key=lambda x: x[1])

        for k, v in generate_from:
            # only for field names which are in Passport model and EXTRA_FIELDS
            if k in passport_field_names or k in EXTRA_SEARCH_FIELDS:
                self.fields[k] = forms.CharField(required=False, label=v)

class SearchSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        """
        :return: form for select search fields
        """
        super(SearchSelectForm, self).__init__(*args, **kwargs)
        form_fields = {}
        [form_fields.update({field.name: field.help_text}) for field in Passport._meta.fields if field.name != "id"]
        # add extra fields
        form_fields.update(EXTRA_SEARCH_FIELDS)

        # convert to unicode
        for key, value in form_fields.items():
            form_fields[key] = smart_text(value)

        form_fields = sorted(form_fields.items(), key=lambda x: x[1])

        for name, help_text in form_fields:
            if name in DEFAULT_SEARCH_TRUE_VALUES.keys():
                self.fields[name] = forms.BooleanField(required=False, label=help_text, initial=True)
            else:
                self.fields[name] = forms.BooleanField(required=False, label=help_text)

