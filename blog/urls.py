from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post, create_post_comment, blogpost_comment_report,\
    super_admin_blog, post_toggle_hide

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/postcomment/$', create_post_comment, name='post_comment'),
    url(r'^(?P<pk>\d+)/reportpostcomment/$',
        blogpost_comment_report, name='blogpost_comment_report'),

    url(r'^superadminblog/$', super_admin_blog, name='super_admin_blog'),
    url(r'^(?P<pk>\d+)/posttogglehide/$',
        post_toggle_hide, name='post_toggle_hide'),
]
