from django.conf.urls import url

from . import views

app_name = 'channelnest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^video/(?P<video_id>[a-f0-9]+)/$', views.video, name='video'),
    url(r'^video-submit$', views.videoSubmit, name='videoSubmit'),
    url(r'^video-check$', views.videoCheck, name='videoCheck'),
]