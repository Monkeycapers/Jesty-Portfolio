from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.apps import apps
import json, os

from posts.models import Post, Tag, Comment

# Create your views here.

def ajax(request, page):
    template = loader.get_template('posts/ajaxposts.j2')
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

pride_colors = ['#e40303', '#ff8c00', '#ffed00', '#008026', '#004dff', '#750787'] #LGBTQ color codes
pride_height=6
pride_width=5

#misc things to add to context
def wrapContext(context):
    pride_colors_info = []
    for index,col in enumerate(pride_colors):
        pride_colors_dict = {
          'y': index * pride_height,
          'x': 0,
          'width': pride_width,
          'height': pride_height,
          'col': col
        }
        pride_colors_info.append(pride_colors_dict)
    context['pride_colors'] = pride_colors_info
    return context

def togglenight(request):
    dark = request.session['dark'] if 'dark' in request.session else False
    request.session['dark'] = not dark
    print('TOGGLE_NIGHT')
    return HttpResponse(status=200)

def showResume(request):
    PATH_TO_RESUME = os.path.join(apps.get_app_config('posts').path, 'res/resume.pdf')
    return FileResponse(open(PATH_TO_RESUME, 'rb'))

def projects(request):
    dark = request.session['dark'] if 'dark' in request.session else False
    return render(request, 'posts/projects.j2', wrapContext({
        'hidesidebar':False,
        'fullwidth':False,
        'dark': dark
    }))

def drawit(request):
    dark = request.session['dark'] if 'dark' in request.session else False
    return render(request, 'posts/drawit.j2', wrapContext({
        'hidesidebar':True,
        'fullwidth':True,
        'dark': dark
    }))

def index(request):
    return getPosts(5, 1, request)

def getPosts(amount, page, request):
    print('dark' in request.session)
    dark = request.session['dark'] if 'dark' in request.session else False
    #print(dark)
    return render(request, 'posts/posts.j2', getContext(amount, page, True, dark))

def postsByTag(request, tag, amount=5, page=1):
    actualTag = Tag.objects.get(tag=tag)
    print(actualTag)
    posts = Post.objects.filter(tags=actualTag) # todo: very basic
    total = len(posts)
    posts = posts[((page - 1) * amount):(amount + ((page - 1) * amount))]
    dark = request.session['dark'] if 'dark' in request.session else False
    context = {
        'latest_posts_list': posts,
        'more_posts': (len(posts) >= amount),
        'no_posts': (len(posts) == 0),
        'is_home': False,
        'amount': total,
        'dark': dark
    }
    return render(request, 'posts/search.j2', wrapContext(context))

#Render a list of post previews orderd by most recently published
def getContext(amount, page, is_home=True, dark=False):
    latest_posts_list = Post.objects.order_by('-published')[((page - 1) * amount):(amount + ((page - 1) * amount))] # todo: very basic
    context = {
        'latest_posts_list': latest_posts_list,
        'more_posts': (len(latest_posts_list) >= amount),
        'no_posts': (len(latest_posts_list) == 0),
        'is_home': is_home,
        'dark': dark
    }
    return wrapContext(context)

def getPost(request, pid, slug=None):
    print(pid)
    p = Post.objects.get(pk=pid)

    # global comments
    # comments = None
    # if p.allow_comments:
    #     comments = p.comment_set.all()

    comments = p.comment_set.all()

    dark = request.session['dark'] if 'dark' in request.session else False

    content = p.content
    if p.file_path:
        #load content from page
        with open(p.get_file_path_abspath()) as File:
            content = File.read()

    context = {'post': p,
     'is_home': False,
     'tags': p.tags.all(),
     'dark': dark,
     'hidesidebar': not p.toggle_sidebar,
     'comments':comments,
     'text':content,
     'md':p.post_type == 'MD',     
     'amount_comments': len(comments) if p.allow_comments else -1
     }
    return render(request, 'posts/post.j2', wrapContext(context))

def comment(request, pid):

    #todo: check if post allows comments
    print('test')
    data = json.loads(request.body)
    
    p = Post.objects.get(pk=pid)
    comment = Comment(content=data['content'], author_name=data['author'], post=p, published=timezone.now())
    comment.save()
    return HttpResponse(status=200)

def search(request, type=None, searchtext=None, amount=5, page=1):
    print(type)
    print(searchtext)
    dark = request.session['dark'] if 'dark' in request.session else False
    tags = Tag.objects.all()
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
            'tags': tags,
            'latest_posts_list': posts,
            'more_posts': (len(posts) >= amount),
            'no_posts': (len(posts) == 0),
            'is_home': False,
            'amount': total,
            'dark': dark
        }
        return render(request, 'posts/search.j2', wrapContext(context))
    else:
        context = {
            'hastag': False,
            'tags': tags,
            'none': True,
            'no_posts': True,
            'is_home': False,
            'amount': 0,
            'dark': dark
        }
        return render(request, 'posts/search.j2', wrapContext(context))