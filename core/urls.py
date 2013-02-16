from core.views import PassportDetailView, PassportUpdateView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^view/(?P<pk>\d+)$',  PassportDetailView.as_view()),
    url(r'^edit/(?P<pk>\d+)$',  PassportUpdateView.as_view(), name="edit"),
)
