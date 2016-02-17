from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^slice_(?P<slice_id>[0-9]+)/$', views.workspace, name='workspace'),
    url(r'^slice_(?P<slice_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'^addLink/$', views.addLink, name='addLink'),
]