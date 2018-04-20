from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
	url(r'^a_post_list/(?P<pk>\w+)/$', views.a_post_list, name='a_post_list'),
	url(r'^accounts/login/$', views.login, {'template_name': 'blog/login.html'}, name='login' ),
    url(r'^accounts/logout/$', views.logout, {'template_name': 'blog/logout.html'}, name='logout' ),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]