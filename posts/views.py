from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Post, Tag

# Create your views here.

def ajax(request, page):
    template = loader.get_template('posts/ajaxposts.html')
    context = getContext(5, page)
    output = template.render(context, request)
    return JsonResponse(
    {
        "html": output,
        "page": page,
        "more_posts": context['more_posts'],
        "no_posts": context['no_posts']
    }
    )

def index(request):
    return getPosts(5, 1, request)

def getPosts(amount, page, request):
    return render(request, 'posts/posts.html', getContext(amount, page))

def postsByTag(request, tag, amount=5, page=1):
    actualTag = Tag.objects.get(tag=tag)
    print(actualTag)
    posts = Post.objects.filter(tags=actualTag) # todo: very basic
    total = len(posts)
    posts = posts[((page - 1) * amount):(amount + ((page - 1) * amount))]
    context = {
        'latest_posts_list': posts,
        'more_posts': (len(posts) >= amount),
        'no_posts': (len(posts) == 0),
        'is_home': False,
        'amount': total
    }
    return render(request, 'posts/search.html', context)

def getContext(amount, page, is_home=True):
    latest_posts_list = Post.objects.order_by('-published')[((page - 1) * amount):(amount + ((page - 1) * amount))] # todo: very basic
    context = {
        'latest_posts_list': latest_posts_list,
        'more_posts': (len(latest_posts_list) >= amount),
        'no_posts': (len(latest_posts_list) == 0),
        'is_home': is_home
    }
    return context

def getPost(request, pid, slug=None):
    print(pid)
    p = Post.objects.get(pk=pid)
    context = {'post': p,
     'is_home': False,
     'tags': p.tags.all()
     }
    return render(request, 'posts/post.html', context)

def search(request, type=None, searchtext=None, amount=5, page=1):
    print(type)
    print(searchtext)
    if (type == 'tag'):
        print('?')
        try:
            actualTag = Tag.objects.get(tag=searchtext)
        except ObjectDoesNotExist:
            actualTag = None
        
        posts = Post.objects.filter(tags=actualTag) # todo: very basic, use regex (tag1&tag2&tag3)
        total = len(posts)
        posts = posts[((page - 1) * amount):(amount + ((page - 1) * amount))]
        context = {
            'hastag': True,
            'tag': actualTag,
            'latest_posts_list': posts,
            'more_posts': (len(posts) >= amount),
            'no_posts': (len(posts) == 0),
            'is_home': False,
            'amount': total
        }
        return render(request, 'posts/search.html', context)
    else:
        context = {
            'hastag': False,
            'none': True,
            'no_posts': True,
            'is_home': False,
            'amount': 0
        }
        return render(request, 'posts/search.html', context)