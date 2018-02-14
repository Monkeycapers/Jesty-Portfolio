from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() # Content is shown only when viewing the post
    preview = models.TextField() # Preview, shown when: searching for posts or at home
    published = models.DateTimeField('date published')
    post_id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = Author
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    posts = models.ManyToManyField(Post, blank=True)
    def __str__(self):
        return self.name
