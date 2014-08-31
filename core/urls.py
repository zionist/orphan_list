from core.views.passport import PassportDetailView, PassportUpdateView, \
        PassportDeleteView, PassportListView, PassportCreateView
from core.views.select import SearchSelectView, XlsSelectView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^view/(?P<pk>\d+)$',  PassportDetailView.as_view(), name="view"),
    url(r'^update/(?P<pk>\d+)$', PassportUpdateView.as_view(),
        name="update"),
    url(r'^delete/(?P<pk>\d+)$', PassportDeleteView.as_view(), name="delete"),
    url(r'^create$', PassportCreateView.as_view(), name="create"),
    url(r'^list/$', PassportListView.as_view(), name="list"),
    url(r'^select/search/$', SearchSelectView.as_view(), name="select.search"),
    url(r'^select/xls/$', XlsSelectView.as_view(), name="select.xls"),
    url(r"^login/$", "django.contrib.auth.views.login",
        {"template_name": "login.html"}),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login",
        {"login_url": "/login", "extra_context": {"title": "true"}})
)
