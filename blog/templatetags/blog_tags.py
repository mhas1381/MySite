from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name='postsCount')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name='postTitles')
def function():
    posts = Post.objects.filter(status = 1)
    return posts

@register.filter
def snippet(content , arg = 15):
    return content[:arg]

@register.inclusion_tag('blog/popularPosts.html')
def popularPosts():
    posts = Post.objects.filter(status =1 ).order_by('-published_date')[:3]
    return {'posts':posts}