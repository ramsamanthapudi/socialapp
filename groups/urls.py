from django.urls import path,re_path
from . import views

app_name='groups'

urlpatterns = [
    path('',views.GroupList.as_view(),name='list'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    #re_path('posts/in/(?P<slug>[\w-]+)/$', views.GroupDetail.as_view(),name='detail'),
    path('detail/<int:pk>',views.GroupDetail.as_view(),name='detail'),
    path('join/<int:pk>', views.JoinGroup.as_view(),name='join'),
    path('leave/<int:pk>', views.LeaveGroup.as_view(), name='leave')
]