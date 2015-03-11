from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bootstrap_lti.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^lti_tools/basic_lti_app/', include('basic_lti_app.urls', namespace="basic_lti_app")),
    url(r'^lti_tools/auth_error/', 'bootstrap_lti.views.lti_auth_error', name='lti_auth_error'),
)
