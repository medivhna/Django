from django.conf.urls import patterns, include, url
from mysite.views import hours_ahead, current_datetime

urlpatterns = patterns('',
	('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)

