from django.conf.urls import url, include
from accounts.views import acc_index, logout, login, registration, user_profile, get_order_details, validate_username
from accounts import url_reset

urlpatterns = [
    url(r'^acc_index/$', acc_index, name="acc_index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="user_profile"),
    url(r'^(?P<pk>\d+)/orders/$', get_order_details, name='get_order_details'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
]
