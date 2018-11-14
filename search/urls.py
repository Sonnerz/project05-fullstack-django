from django.conf.urls import url
from .views import do_search, do_search_ref, do_search_blog

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^ref/$', do_search_ref, name='search_ref'),
    url(r'^blogsearch/$', do_search_blog, name='search_blog')
]
