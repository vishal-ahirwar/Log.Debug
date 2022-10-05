from django.shortcuts import render, get_object_or_404
from .models import Post,Status
# Create your views here.

#list of Posts
def PostList(request):
    Posts=Post.objects.all().exclude(status=Status.DRAFT)
    context={"Posts":Posts}
    return render(request,"Post/Home.html",context)

#detail of specific post
def PostDetail(request,Pk):
    Post_=get_object_or_404(Post,pk=Pk,status=Status.PUBLISHED)
    context={"Post":Post_}
    return render(request,"Post/Detail.html",context)

