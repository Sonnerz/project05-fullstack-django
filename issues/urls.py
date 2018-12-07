
from django.conf.urls import url

from issues.views import get_all_bugs, bug_detail,\
    create_bug, edit_bug, vote_bug,\
    get_all_features, feature_detail,\
    new_feature, edit_feature, bug_comment_report,\
    super_admin, comment_toggle_hide, admin_edit


urlpatterns = [
    url(r'^$', get_all_bugs, name='get_all_bugs'),
    url(r'^(?P<pk>\d+)/editbug/$', edit_bug, name='edit_bug'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^newbug/$', create_bug, name='create_bug'),
    url(r'^(?P<pk>\d+)/vote/$', vote_bug, name='vote_bug'),

    url(r'^all_features$', get_all_features, name='get_all_features'),
    url(r'^(?P<pk>\d+)/features/$', feature_detail, name='feature_detail'),
    url(r'^(?P<pk>\d+)/editfeature/$', edit_feature, name='edit_feature'),
    url(r'^newfeature/$', new_feature, name='new_feature'),

    url(r'^(?P<pk>\d+)/bugcommentreport/$',
        bug_comment_report, name='bug_comment_report'),

    url(r'^superadmin/$', super_admin, name='super_admin'),
    url(r'^(?P<pk>\d+)/commenttogglehide/$',
        comment_toggle_hide, name='comment_toggle_hide'),
    url(r'^(?P<pk>\d+)/adminedit/$',
        admin_edit, name='admin_edit'),
]
