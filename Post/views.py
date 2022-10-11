from django.shortcuts import render, get_object_or_404
from .models import Post,Status,Comment
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import CommentForm, EmailPostForm
from django.core.mail import send_mail
from django.views.decorators.http import require_Post

# Create your views here.
@require_Post
def PostComment(request,post_id):
    post=get_object_or_404(Post,id=post_id,status=Status.PUBLISHED)
    comment=None
    form=CommentForm(data=request.POST)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post=post
        comment.save()
    return render(request,'Post/Comment.html',{'post':post,'form':form})

def SharePost(request,post_id):
    post=get_object_or_404(Post,id=post_id,status=Status.PUBLISHED)
    if request.method=='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            send_mail("Test Mail","This is a Test Email from django Application",cd['email'],list(cd['to']))
    else:
        form=EmailPostForm()
    return render(request,'Post/Share.html',{'post':post,'form':form})

#list of Posts
class PostListView(ListView):
    '''
    Alternative Post List View
    '''
    queryset=Post.objects.all()
    context_object_name='Posts'
    template_name='Post/Home.html'

def PostList(request):

    Posts=Post.objects.all().exclude(status=Status.DRAFT)
    # paginator=Paginator(Posts,3)
    # PageNumber=request.Get.get('page',1)
    # Posts=paginator.page(PageNumber)
    context={"Posts":Posts}
    return render(request,"Post/Home.html",context)

#detail of specific post
def PostDetail(request,Pk):
    Post_=get_object_or_404(Post,pk=Pk,status=Status.PUBLISHED)
    context={"Post":Post_}
    return render(request,"Post/Detail.html",context)


