from multiprocessing import context
from operator import ge
from unicodedata import category, name
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def blog_view(request ,**kwargs):
    posts = Post.objects.filter(status =1)
    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None :
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
    
    posts = Paginator(posts , 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = Paginator.page(1)
    except EmptyPage:
        posts = Paginator.page(1)

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

def blog_search(request):
    # print(request.__dict__)
    posts = Post.objects.filter(status = 1)
    if request.method =='GET':
        # print('its get request')
        posts = posts.filter(content__contains = request.GET.get('s'))
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html' , context)