from django.contrib import admin

from .models import Post, Tag, Author

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Author)

# Register your models here.
