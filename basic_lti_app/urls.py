from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url(r'^$', 'basic_lti_app.views.index', name='index'),
    url(r'^index.html$', 'basic_lti_app.views.index', name='index2'),
    url(r'^lti_launch$', 'basic_lti_app.views.lti_launch', name='lti_launch'),
    url(r'^main$', 'basic_lti_app.views.main', name='main'),
    url(r'^tool_config$', 'basic_lti_app.views.tool_config', name='tool_config'),
)
