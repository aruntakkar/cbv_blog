from django.conf.urls import url
from .views import PostListing, PostCreate, PostDetail, PostUpdate, PostDelete

urlpatterns = [
	url(r'^$', PostListing.as_view(), name='listing'),
	url(r'^create/$', PostCreate.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/update/$', PostUpdate.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='delete'),
]