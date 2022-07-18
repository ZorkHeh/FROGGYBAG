from django.contrib import admin

from apps.blog.models import Article, BlogCategory, Tag

admin.site.register(Article)
admin.site.register(BlogCategory)
admin.site.register(Tag)
