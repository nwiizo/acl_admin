from django.conf.urls import url
from cms import views

urlpatterns = [
    # ACL
    url(r'^acl/$', views.acl_list, name='acl_list'),   # 一覧
    url(r'^acl/add/$', views.acl_edit, name='acl_add'),  # 登録
    url(r'^acl/mod/(?P<book_id>\d+)/$', views.acl_edit, name='acl_mod'),  # 修正
    url(r'^acl/del/(?P<book_id>\d+)/$', views.acl_del, name='acl_del'),   # 削除
        ]
