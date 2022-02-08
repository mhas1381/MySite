from unicodedata import category
from django import template
from blog.models import Post,Category

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

@register.inclusion_tag('blog/latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(status =1 ).order_by('-published_date')[:4]
    return {'posts':posts}

@register.inclusion_tag('blog/post-categories.html')
def post_categories():
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories':cat_dict}    