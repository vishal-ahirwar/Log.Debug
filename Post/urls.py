from django.urls import path
from .views import PostDetail,PostList,PostListView,SharePost

app_name="Post"

urlpatterns=[
    path('',PostListView.as_view(),name='home'),
    path('/<int:Pk>',PostDetail,name="detail"),
    path('share/<int:post_id>',SharePost,name='share'),
]