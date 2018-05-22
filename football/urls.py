from django.conf.urls import url
from . import views

app_name = 'football'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<footballclub_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<footballplayers_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^footballplayers/(?P<filter_by>[a-zA_Z]+)/$', views.footballplayers, name='footballplayers'),
    url(r'^create_footballclub/$', views.create_footballclub, name='create_footballclub'),
    url(r'^(?P<footballclub_id>[0-9]+)/create_footballplayer/$', views.create_footballplayer, name='create_footballplayer'),
    #url(r'^create_footballplayer/$', views.create_footballplayer, name='create_footballplayer'),
    url(r'^(?P<footballclub_id>[0-9]+)/delete_footballplayer/(?P<footballplayer_id>[0-9]+)/$', views.delete_footballplayer, name='delete_footballplayer'),
    #url(r'^(?P<footballclub_id>[0-9]+)/favorite_footballclub/$', views.favorite_footballclub, name='favorite_footballclub'),
    url(r'^(?P<footballclub_id>[0-9]+)/delete_footballclub/$', views.delete_footballclub, name='delete_footballclub'),
]