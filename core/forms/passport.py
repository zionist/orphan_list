from django.forms import ModelForm
from core.models.passport import Passport

class PassportForm(ModelForm):
    class Meta:
        model = Passport
