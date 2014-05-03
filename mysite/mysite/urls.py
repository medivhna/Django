from django.conf.urls import patterns, include, url
from mysite.views import hours_ahead

urlpatterns = patterns('',
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)

