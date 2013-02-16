from core.views import PassportView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',                                                           
    #url(r'^$', views.index, name='index'), 
    url(r'^view/(?P<index>\d+)$',  PassportView.as_view()),                       
)                                                                                    
