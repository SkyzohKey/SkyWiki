from django.conf.urls import include, url
from . import views

"""
urlpatterns = [
    url(r'^$', views.browse, name='home'),
    url(r'^(?P<page>[a-zA-Z0-9]+)(?:/)$', views.browse, name='browse'),
    url(r'^(?P<category>[a-zA-Z0-9]+):(?P<page>[a-zA-Z0-9]+)(?:/)$', views.browse, name='browse')
]
"""

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^(?P<page>[a-zA-Z0-9\-]+)/$', views.standalonePage, name='page'),
    url(r'^(?P<category>[a-zA-Z0-9\-]+)/(?P<page>[a-zA-Z0-9\-]+)/$', views.categorizedPage, name='catPage')
]
