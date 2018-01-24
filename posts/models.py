from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40) # Slug is no space url
    content = models.TextField() # Content is shown only when viewing the post
    preview = models.TextField() # Preview, shown when: searching for posts or at home
    published = models.DateTimeField('date published')
    post_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.title
