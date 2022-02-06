from operator import ge
from unicodedata import name
from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.

def blog_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request ,'blog/blog-home.html' , context )
def blog_single(request , pid):
    post = get_object_or_404(Post , pk=pid , status =1)
    context = {'post':post}
    return render(request ,'blog/blog-single.html',context )

def test(request , pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post , pk=pid)
    context = {'ppst':post}
    return render(request , 'test.html' , context)
    