from django.conf.urls import url
from issues.views import get_all_bugs, bug_detail, create_or_edit_bug

urlpatterns = [
    url(r'^$', get_all_bugs, name='get_all_bugs'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
]
