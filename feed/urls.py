from django.conf.urls import url 
from . import views


urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^friends/(?P<pk>[0-9]+)/$',views.friends,name='friends'),
	url(r'^profile/(?P<pk>[0-9]+)/$',views.profile,name='profile'),
	url(r'^friends/profile/(?P<name>[a-zA-Z0-9]+)/',views.fprofile,name='f-profile'),
	url(r'^profile/(?P<user_id>[0-9]+)/add/$',views.add_profile,name='add-profile'),
]