from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile, get_order_details
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="user_profile"),
    url(r'^(?P<pk>\d+)/orders/$', get_order_details, name='get_order_details'),
    url(r'^password-reset/', include(url_reset))
]
