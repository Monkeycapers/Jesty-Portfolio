from django.db import models
from django.utils import timezone
from django.apps import apps
import os
from relativefilepathfield.fields import RelativeFilePathField

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.tag

class Post(models.Model):
    POST_TYPES = (
        ('MD', 'Markdown'), #Markdown content, stored in db and converted to html later
        ('HTML', 'HTML') #HTML content
    )
    title = models.CharField(max_length=200)
    post_type = models.TextField(choices=POST_TYPES)
    file_path = RelativeFilePathField(path=os.path.join(apps.get_app_config('posts').path, 'pages'), blank=True) #if not set load from content
    content = models.TextField() # Content is shown only when viewing the post
    preview = models.TextField() # Preview, shown when: searching for posts or at home
    published = models.DateTimeField('date published')
    post_id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField('Tag', blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True )
    allow_comments = models.BooleanField()
    toggle_sidebar = models.BooleanField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    published = models.DateTimeField('date published')
    author_name = models.CharField(max_length=20)
    #Todo: Proper author support author = models.CharField(max_length=20) 
    def __str__(self):
        return self.content

    # @classmethod
    # def create(cls, content, author_name, post):
    #     comment = cls(content=content, author_name=author_name, post=post, published=timezone.now())
    #     return comment

class Author(models.Model):
    name = models.CharField(max_length=200)
    #posts = models.ManyToManyField('Post', blank=True)
    def __str__(self):
        return self.name
