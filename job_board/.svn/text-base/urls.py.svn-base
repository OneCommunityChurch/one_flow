from django.conf.urls.defaults import patterns, include, url
from one_flow.job_board.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'one_flow.views.home', name='home'),
    # url(r'^one_flow/', include('one_flow.foo.urls')),

    url(r'^$', index),
    url(r'^logout$', logout),
    url(r'^job_list$', job_list),
    url(r'^job_edit/(\d+)/$', job_edit),
    url(r'^job_edit$', job_edit),
    url(r'^job_edit/$', job_edit),
    url(r'^job_delete/(\d+)/$', job_delete),
    url(r'^job_view/(\d+)/$', job_view),
    url(r'^company_list$', company_list),
    url(r'^company_submit$', company_job_submit),
    url(r'^post/', company_job_submit),
    url(r'^company_edit/(\d+)/$', company_edit),
    url(r'^company_edit$', company_edit),
    url(r'^company_delete/(\d+)/$', company_delete),
    url(r'^company_view/(\d+)/$', company_view),


)
