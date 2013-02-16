from django.views.generic.edit import (CreateView,
        UpdateView, DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from core.forms.passport import PassportForm
from core.models import Passport
from django.conf import settings

# context interface class
class ContextField():
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PassportDetailView(DetailView):
    def __init__(self):
        super(PassportDetailView, self).__init__()
    model = Passport
    template_name = 'view.html'

    # authication here
    def get_object(self):
        object = super(DetailView, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super(PassportDetailView, self).get_context_data(**kwargs)
        #dynamicly generate context from model fields
        # pass help text from models to context
        fields = []
        for field in self.object._meta.fields:
            if field.name == "id":
                continue
            help_text = \
                    self.object._meta.\
                    get_field_by_name(field.name)[0].help_text
            value = field.value_from_object(self.object) or ""
            fields.append(ContextField(help_text, value))
        context["passport_fields"] = fields

        # title
        context["title"] = self.object.__unicode__
        return context


class PassportFormView(FormView):
    def __init__(self):
        super(PassportView, self).__init__()
    template_name = 'view.html'
    form_class = PassportForm
    model = Passport
    success_url = "/thanks/"

    def dispatch(self, request, *args, **kwargs):
       print request.__dict__
       return super(PassportView, self).dispatch(request, *args, **kwargs)

    def form_is_valid(self, form):
        print form.__dict__
        print form.save()
        return super(PassportView, self).form_valid(form)

    def get_absolute_url(self):
        return reverse('view', kwargs={'index': self.pk})

    def get_object(self, queryset=None):
        print "# object"
        obj = Passport.objects.get(id=self.kwargs['index'])

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        return context
