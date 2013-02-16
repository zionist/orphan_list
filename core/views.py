from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from core.forms.passport import PassportForm
from core.models import Passport


class PassportView(FormView):
    
    def __init__(self):
        super(PassportView, self).__init__()
        print "#"
    
    template_name = 'view.html'
    form_class = PassportForm
    model = Passport
    success_url = "/thanks/"

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
