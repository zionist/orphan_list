import xlwt
from datetime import date
from django.http import HttpResponse
from django.views.generic.edit import (CreateView,
        UpdateView, DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from core.forms.passport import PassportForm
from core.forms.search import QuickSearchForm
from core.models import Passport
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


#dynamicly generate context from model fields
# pass help text from models to context
def get_name_value_from_object(object):
    fields = []
    for field in object._meta.fields:
        if field.name == "id":
            continue
        help_text = \
                object._meta.\
                get_field_by_name(field.name)[0].help_text
        value = field.value_from_object(object) or ""
        fields.append(ContextField(help_text, value))
    return fields


# context interface classes
class ContextField():
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PassportDetailView(DetailView):
    def __init__(self):
        super(PassportDetailView, self).__init__()
    model = Passport
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super(PassportDetailView, self).get_context_data(**kwargs)
        context["passport_fields"] = get_name_value_from_object(self.object)

        # title
        context["title"] = self.object.__unicode__
        return context


class PassportUpdateView(UpdateView):
    def __init__(self):
        super(PassportUpdateView, self).__init__()
    template_name = 'update.html'
    model = Passport

    def get_success_url(self):
        return reverse('update', kwargs={'pk': self.object.pk})
    
    @method_decorator(permission_required("core.change_passport"))
    def dispatch(self, *args, **kwargs):
        return super(PassportUpdateView, self).dispatch(*args, **kwargs)


class PassportDeleteView(DeleteView):
    model = Passport
    template_name="delete.html"

    def get_context_data(self, **kwargs):
        context = super(PassportDeleteView, self).get_context_data(**kwargs)
        context["title"] = self.object.__unicode__
        return context

    def get_success_url(self):
        return reverse('list')

    @method_decorator(permission_required("core.delete_passport"))
    def dispatch(self, *args, **kwargs):
        return super(PassportDeleteView, self).dispatch(*args, **kwargs)


class PassportCreateView(CreateView):
    model = Passport
    template_name="create.html"

    def get_success_url(self):
        return reverse('update', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # print '# valid'
        form.save()
        return super(PassportCreateView, self).form_valid(form)

    def form_invalid(self, form):
        # print '# invalid'
        # print form.errors
        return super(PassportCreateView, self).form_invalid(form)

    @method_decorator(permission_required("core.add_passport"))
    def dispatch(self, *args, **kwargs):
        return super(PassportCreateView, self).dispatch(*args, **kwargs)


class PassportListView(ListView):
    model=Passport
    template_name="list.html"
    paginate_by = 20 

    def to_exel(context):
        """
        :param: args  - cleared data from quick_seach form
        """
        # get help_text as names from model
        objects = []
        for object in context.object_list:
            fields = get_name_value_from_object(object)
            objects.append(fields)

        # create 
        book = xlwt.Workbook(encoding='utf8')
        sheet = book.add_sheet('untitled')
        style_plain = xlwt.Style.default_style
        style_bold = xlwt.easyxf("font: bold 1")
        date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

        response = HttpResponse(mimetype='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=list.xls'

        # write header
        for column_index, field in enumerate(objects[0]):
            sheet.write(0, column_index, field.name, style_bold) 

        # write values
        for row_index, fields in enumerate(objects):
            for column_index, field in enumerate(fields):
                if isinstance(field.value, date):
                    style = date_style

                else:
                    style = style_plain
                sheet.write(row_index + 1, column_index, field.value, 
                style) 
            
        book.save(response)
        return response
        
    def get_context_data(self, **kwargs):
        context = super(PassportListView, self).get_context_data(**kwargs)
        context["title"] = "List"
        context["quick_search_form"] = QuickSearchForm(self.request.GET)
        url = self.request.get_full_path()
        if self.request.GET:
            context["xls_path"] = url + "&xls=yes"
        else:
            context["xls_path"] = url + "?xls=yes"
        return context

    def get(self, request, **kwargs):
        return super(PassportListView, self).get(request, **kwargs)

    def get_queryset(self):
        quick_search_form = QuickSearchForm(self.request.GET)
        if not quick_search_form.is_valid():
            return super(PassportListView, self).get_queryset()
        else:
            args = quick_search_form.cleaned_data
            for k, v in args.items():
                if not v:
                    del args[k] 
            if args:
                return Passport.objects.filter(**args)
            else: 
                return super(PassportListView, self).get_queryset()

    def render_to_response(self, context):
        if self.request.GET.get("xls"):
            return self.to_exel()
        return super(PassportListView, self).render_to_response(context)
        
