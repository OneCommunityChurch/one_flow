from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from job_board.views import company_job_submit
from one_flow.job_board.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'one_flow.views.home', name='home'),
    # url(r'^one_flow/', include('one_flow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', login),
    url(r'^project_manager/', include('project_manager.urls')),
    url(r'^one_info/', include('one_info.urls')),
    url(r'^boxoffice/', include('boxoffice.urls')),
    url(r'^job_board/', include('job_board.urls')),
    url(r'^post/', company_job_submit),
    url(r'^richtext/', include('richtext.urls')),


)
