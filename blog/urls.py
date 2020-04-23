from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
	re_path(r'^a_post_list/(?P<pk>\w+)/$', views.a_post_list, name='a_post_list'),
	re_path(r'^accounts/login/$', LoginView.as_view(template_name='blog/login.html'), name='login' ),
    re_path(r'^accounts/logout/$', LogoutView.as_view(template_name='blog/logout.html'), name='logout' ),
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/delete$', views.post_delete, name='post_delete'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]