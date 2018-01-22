from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

# Create your views here.

def ajax(request, page):
    return render(request, 'posts/ajaxposts.html', getContext(5, page))

def index(request):
    return getPosts(5, 1, request)

def getPosts(amount, page, request):
    return render(request, 'posts/posts.html', getContext(amount, page))

def getContext(amount, page):
    latest_posts_list = Post.objects.order_by('-published')[((page - 1) * amount):(amount + ((page - 1) * amount))] # todo: very basic
    context = {'latest_posts_list': latest_posts_list}
    return context
