from core.views import PassportDetailView, PassportUpdateView, \
        PassportDeleteView, PassportListView, PassportCreateView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^view/(?P<pk>\d+)$',  PassportDetailView.as_view(), name="view"),
    url(r'^update/(?P<pk>\d+)$', PassportUpdateView.as_view(),
        name="update"),
    url(r'^delete/(?P<pk>\d+)$', PassportDeleteView.as_view(), name="delete"),
    url(r'^create$', PassportCreateView.as_view(), name="create"),
    url(r'^list/$', PassportListView.as_view(), name="list"),
)
