from django.conf.urls.defaults import patterns, include, url
from one_flow import project_manager

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'one_flow.views.home', name='home'),
    # url(r'^one_flow/', include('one_flow.foo.urls')),

    url(r'^$', 'project_manager.views.index'),
    url(r'^project$', 'project_manager.views.project'),

)
