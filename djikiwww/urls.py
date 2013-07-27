from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
	(r'^$', RedirectView.as_view(url=u'/wiki/Djiki')),
	(r'^wiki/', include('djiki.urls')),
	url(r'^latest/', 'djiki.contrib.views.latest_changes', name='latest-changes'),
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
		)
