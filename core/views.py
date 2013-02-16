from django.views.generic.edit import (CreateView,
        UpdateView, DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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


class PassportUpdateView(UpdateView):
    def __init__(self):
        super(PassportUpdateView, self).__init__()
    template_name = 'update.html'
    model = Passport

    def dispatch(self, request, *args, **kwargs):
       return super(PassportUpdateView, self).dispatch(request, *args, **kwargs)

    def form_is_valid(self, form):
        print form.__dict__
        print form.save()
        return super(PassportUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('update', kwargs={'pk': self.object.pk})

    def get_object(self):
        object = super(PassportUpdateView, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super(PassportUpdateView, self).get_context_data(**kwargs)
        return context


class PassportDeleteView(DeleteView):
    model = Passport
    template_name="delete.html"

    def get_context_data(self, **kwargs):
        context = super(PassportDeleteView, self).get_context_data(**kwargs)
        context["title"] = self.object.__unicode__
        return context

    def get_success_url(self):
        return reverse('list')


class PassportListView(ListView):
    model=Passport
    template_name="list.html"


    def get_queryset(self):
        query = super(PassportListView, self).get_queryset()
        return query


    def get_context_data(self, **kwargs):
        context = super(PassportListView, self).get_context_data(**kwargs)
        context["title"] = "List"

        return context