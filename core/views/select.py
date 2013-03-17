# -*- coding:utf-8 -*-

foo = 1
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from core.forms.select import SearchSelectForm, XlsSelectForm

class SearchSelectView(FormView):
    template_name = 'search_select_form.html'
    form_class = SearchSelectForm
    success_url = "/core/select/select"

    def get_success_url(self):
        return reverse('select.search')

    def form_valid(self, form):
        self.request.session['select.search'] = form.cleaned_data
        return super(SearchSelectView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        return super(SearchSelectView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SearchSelectView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchSelectView, self).get_context_data(**kwargs)
        if self.request.session.get('select.search'):
            context['form'] = SearchSelectForm(self.request.session['select.search'])
        return context


class XlsSelectView(FormView):
    template_name = 'xls_select_form.html'
    form_class = XlsSelectForm
    success_url = "/core/select/xls"

    def get_success_url(self):
        return reverse('select.xls')

    def form_valid(self, form):
        self.request.session['select.xls'] = form.cleaned_data
        return super(XlsSelectView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        return super(XlsSelectView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(XlsSelectView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(XlsSelectView, self).get_context_data(**kwargs)
        if self.request.session.get('select.xls'):
            context['form'] = XlsSelectForm(self.request.session['select.xls'])
        return context
