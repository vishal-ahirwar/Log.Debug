from django.urls import path
from .views import PostDetail,PostList

app_name="Post"

urlpatterns=[
    path('',PostList,name='home'),
    path('<int:Pk>',PostDetail,name="detail"),
]