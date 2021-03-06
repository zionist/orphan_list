# -*- coding:utf-8 -*-

import xlwt
import urllib
from datetime import date

import reversion
from django.utils.encoding import smart_text
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic.edit import (CreateView,
        UpdateView, DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from core.forms.select import SearchForm
from core.models import Passport
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from common.constants import DEFAULT_SEARCH_TRUE_VALUES, EXTRA_SEARCH_FIELDS


# dynamicly generate context from model fields
# pass help text from models to context
def get_name_value_from_object(object, xls=False, request=None):
    """
    :param object: QuerySet
    :param xls: if True filter by XlsSelectForm stored in session
    :param request: django request object
    :return: list of ContestField
    """
    fields = []
    for field in object._meta.fields:
        if field.name == "id":
            continue
        help_text = \
                object._meta.\
                get_field_by_name(field.name)[0].help_text
        value = field.value_from_object(object) or ""
        if not xls:
            fields.append(ContextField(help_text, value))
        else:
            # filter according XlsSelectForms
            if request.session.get('select.xls'):
                for k, v in request.session['select.xls'].items():
                    if k == field.name and v is True:
                        fields.append(ContextField(help_text, value))
            # default xls select settings
            # show all columns
            else:
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

    # check access for owner. Only owner can modify own data.
    def get(self, request, *args, **kwargs):
        pk = request.resolver_match.kwargs.get('pk')
        obj = Passport.objects.get(pk=pk)
        if not request.user.is_staff:
            if obj.owner != request.user.username:
                return HttpResponseForbidden()
        return super(PassportDetailView, self).get(request, *args, **kwargs)
        
    @method_decorator(login_required)
    # check access for owner. Only owner can modify own data.
    def dispatch(self,request, *args, **kwargs):
        pk = request.resolver_match.kwargs.get('pk')
        obj = Passport.objects.get(pk=pk)
        if not request.user.is_staff:
            if obj.owner != request.user.username:
                return HttpResponseForbidden()
        return super(PassportDetailView, self).dispatch(request, *args, **kwargs)


class PassportUpdateView(UpdateView):
    def __init__(self):
        super(PassportUpdateView, self).__init__()
    template_name = 'update.html'
    model = Passport

    def get_success_url(self):
        return reverse('update', kwargs={'pk': self.object.pk})

    # get owner from object and set it
    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        pk = request.resolver_match.kwargs.get('pk')
        obj = Passport.objects.get(pk=pk)
        post.update({"owner": obj.owner})

        request.POST = post
        return super(PassportUpdateView, self).post(request, *args, **kwargs)

    # check access for owner. Only owner can modify own data.
    @method_decorator(permission_required("core.change_passport"))
    def dispatch(self,request, *args, **kwargs):
        pk = request.resolver_match.kwargs.get('pk')
        obj = Passport.objects.get(pk=pk)
        if not request.user.is_staff:
            if obj.owner != request.user.username:
                return HttpResponseForbidden()
        return super(PassportUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        version_list = reversion.get_unique_for_object(self.object)
        if version_list:
            version = version_list[0]
            # get difference between last version and new version
            diff = {}
            for k,v in version.field_dict.iteritems():
                if v not in form.cleaned_data.values():
                    if k != u"id":
                        diff[k] = form.cleaned_data[k]
            # get the help_text of the field using name
            for k,v in diff.items():
                for field in Passport._meta.fields:
                    if field.name == k:
                        diff[smart_text(field.help_text)] = v
                        del diff[k]
            with reversion.create_revision():
                form.save()
                changed = u"Изменено: "
                for k, v in diff.items():
                    changed += u" %s -> %s | " % (k, v)
                reversion.set_comment(changed)
        else:
            with reversion.create_revision():
                form.save()
            
        return super(PassportUpdateView, self).form_valid(form)


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
    def dispatch(self,request, *args, **kwargs):
        pk = request.resolver_match.kwargs.get('pk')
        obj = Passport.objects.get(pk=pk)
        if not request.user.is_staff:
            if obj.owner != request.user.username:
                return HttpResponseForbidden()
        return super(PassportDeleteView, self).dispatch(request, *args, **kwargs)


class PassportCreateView(CreateView):
    model = Passport
    template_name="create.html"

    def get_success_url(self):
        return reverse('update', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.save()
        return super(PassportCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(PassportCreateView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        # set default value
        post.update({"owner": request.user.username})
        request.POST = post
        return super(PassportCreateView, self).post(request, *args, **kwargs)

    @method_decorator(permission_required("core.add_passport"))
    def dispatch(self, *args, **kwargs):
        return super(PassportCreateView, self).dispatch(*args, **kwargs)


class PassportListView(ListView):
    model=Passport
    template_name="list.html"
    paginate_by = 20

    def create_search_form_data(self, data):
        """
        Create dynamic passport search form from input dict and EXTRA_SEARCH_FIELDS
        :param data:
        :return:
        """
        # get help_text from Passport model
        search_form_generate_from = {}
        for name, value in data.items():
            if name in Passport._meta.get_all_field_names() and value:
                field = Passport._meta.get_field_by_name(name)[0]
                search_form_generate_from[name] = field.help_text

        # add extra fields
        for key, value in EXTRA_SEARCH_FIELDS.items():
            if data.get(key):
                search_form_generate_from[key] = value
        return search_form_generate_from

    def to_exel(self):
        """
        :param: args  - cleared data from seach form
        """
        # get help_text as names from model
        objects = []
        for object in self.object_list:
            fields = get_name_value_from_object(object, xls=True,
                                                request=self.request)
            # filter results according XlsSelectForm in session
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
        # get session select form and set search form according it
        if self.request.session.get("select.search"):
            form_data = self.request.session["select.search"]
        else:
            form_data = DEFAULT_SEARCH_TRUE_VALUES

        search_form_generate_from = self.create_search_form_data(form_data)

        context["search_form"] = SearchForm(self.request.GET.copy(), generate_from=search_form_generate_from)
        url = self.request.get_full_path()
        if self.request.GET:
            context["xls_path"] = url + "&xls=yes"
        else:
            context["xls_path"] = url + "?xls=yes"

        # get url of request and pass it to template for correct list pagination
        get = self.request.GET.copy()
        if get:
            if get.get("page"):
                get.pop("page")
            get_utf_8 = {}
            for k, v in get.items():
                get_utf_8[k] = v.encode("utf-8")
            url = urllib.urlencode(get_utf_8)
            context["paginate_url"] = url
        # get count of all Passports
        context["count"] = self.object_list.count()
        return context

    def get(self, request, **kwargs):
        return super(PassportListView, self).get(request, **kwargs)

    def get_queryset(self):
        data = self.request.GET.copy()

        # search logic
        extra_fields = {}
        for name, value in EXTRA_SEARCH_FIELDS.items():
            if name in data.keys():
                extra_fields[name] = data[name]
                del data[name]

        if self.request.session.get('select.search'):
            form_data = self.request.session["select.search"]
        else:
            form_data = {}
            # set default values if select.search form not set
            for k,v in DEFAULT_SEARCH_TRUE_VALUES.items():
                form_data.update({k: True})

        # create dynamic search form
        search_form_generate_from = self.create_search_form_data(form_data)

        search_form = SearchForm(data, generate_from=search_form_generate_from)
        if not search_form.is_valid():
            return super(PassportListView, self).get_queryset().order_by("surname")
        else:
            args = search_form.cleaned_data or {}
            # all search is case insensitive
            exact_search = False
            if args["exact"] == True:
                exact_search = True
            del args["exact"]
            
            for key,value in args.items():
                if key in EXTRA_SEARCH_FIELDS:
                    del args[key]
                    continue
                # exact search logic
                if value:
                    if exact_search:
                        args[key + "__exact"] = value
                    else:
                        args[key + "__icontains"] = value
                del args[key]
            if extra_fields.get("year"):
                args.update({"birthday__year": extra_fields["year"]})
            if extra_fields.get("from_year"):
                try:
                    from_year = date(int(extra_fields["from_year"]), 1, 1)
                except ValueError:
                    pass
                else:
                    args.update({"birthday__gte": from_year})
            if extra_fields.get("to_year"):
                try:
                    to_year = date(int(extra_fields["to_year"]), 1, 1)
                except ValueError:
                    pass
                else:
                    args.update({"birthday__lte": to_year})

            # we need to search 
            if self.request.user.is_staff:
                return Passport.objects.filter(**args).order_by("surname")
            else:
                return Passport.objects.filter(**args).filter(owner=self.request.user.username).order_by("surname")

    def render_to_response(self, context):
        if self.request.GET.get("xls"):
            return self.to_exel()
        return super(PassportListView, self).render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PassportListView, self).dispatch(*args, **kwargs)
        
