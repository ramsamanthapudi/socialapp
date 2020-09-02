from django.urls import path,re_path

from . import views

app_name = 'posts'

urlpatterns = [
    path('list/',views.PostList.as_view(),name='list'),
    path('new/',views.CreatePost.as_view(), name='create'),
    re_path('by/(?P<username>[-\w]+)',views.UserPosts.as_view(), name='for_user'),
    re_path('by/(?P<username>[-\w]+)/(?P<pk>\d+)/',views.PostDetail.as_view(), name='detail'),
    re_path('delete/(?P<pk>\d+)/$', views.DeletePost.as_view(),name='delete')
]