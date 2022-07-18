from django.contrib import admin

from apps.blog.models import Article, BlogCategory

admin.site.register(Article)
admin.site.register(BlogCategory)
