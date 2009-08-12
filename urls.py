from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

urlpatterns = patterns('',
    url(r'^$', view='files.views.all',
        name="files_all"),

    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', view='files.views.detail',
        name="files_detail"),

    #url(r'^create/$', view='files.views.create',
    #    name="files_create"),

    url(r'^delete/(?P<id>\d+)/', view='files.views.delete',
        name='files_delete'),

    url(r'add/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/$',\
            view='files.views.add', name='files_add'),

    url(r'change/(?P<id>\d+)/', view='files.views.change',
        name='files_change'),

    url(r'for_day/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',\
            view='files.views.for_day', name='files_for_day'),

    url(r'for/(?P<username>[-\w]+)/$',\
            view='files.views.for_user', name='files_for_user'),

    url(r'for/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/$',\
            view='files.views.for_instance', name='files_for_instance'),
)
