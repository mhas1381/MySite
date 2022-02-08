from multiprocessing import context
from operator import ge
from unicodedata import category, name
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

# def test(request , pid):
#     # post = Post.objects.get(id=pid)
#     post = get_object_or_404(Post , pk=pid)
#     context = {'post':post}
#     return render(request , 'test.html' , context)
def test(request):
    return render(request , 'test.html')

def blog_category(request , cat_name):
    posts = Post.objects.filter(status = 1)
    posts = Post.objects.filter(category__name = cat_name)
    context = {'posts':posts}
    return render(request ,'blog/blog-home.html' , context)