from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() # Content is shown only when viewing the post
    preview = models.TextField() # Preview, shown when: searching for posts or at home
    published = models.DateTimeField('date published')
    def __str__(self):
        return self.title
