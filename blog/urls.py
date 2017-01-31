from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #문자열이 아무것도 없는 경우 매칭
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
