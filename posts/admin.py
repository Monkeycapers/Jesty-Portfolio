from django.contrib import admin

from .models import Post, Tag, Author, Comment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)

# Register your models here.
