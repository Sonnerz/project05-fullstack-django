from django.conf.urls import url
from .views import do_search, do_search_ref, do_feat_search, do_feat_search_ref

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^ref/$', do_search_ref, name='search_ref'),
    url(r'^feature/$', do_feat_search, name='feat_search'),
    url(r'^featureref/$', do_feat_search_ref, name='feat_search_ref'),
]
