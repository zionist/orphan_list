# -*- coding:utf-8 -*-

foo = 1
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from core.forms.search import SearchSelectForm

class SearchSelectView(FormView):
    template_name = 'search_select_form.html'
    form_class = SearchSelectForm
    success_url = "/core/search/select"

    def get_success_url(self):
        return reverse('search.select')

    def form_valid(self, form):
        print "# form is valid"
        self.request.session['form_data'] = form.cleaned_data
        print form.cleaned_data
        return super(SearchSelectView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        print "#get"
        return super(SearchSelectView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchSelectView, self).get_context_data(**kwargs)
        if self.request.session.get('form_data'):
            context['form'] = SearchSelectForm(self.request.session['form_data'])
        print context
        return context

