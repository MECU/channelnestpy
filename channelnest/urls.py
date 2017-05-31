from django.conf.urls import include, url

from . import views

app_name = 'channelnest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^video/(?P<video_id>[a-f0-9]+)/$', views.video, name='video'),
    url(r'^video-submit$', views.videoSubmit, name='videoSubmit'),
    url(r'^video-check$', views.videoCheck, name='videoCheck'),
    url(r'^user/(?P<username>[a-zA-Z0-9]+)/$', views.profile, name='profile'),
    url(r'^accounts/', include('allauth.urls')),
]