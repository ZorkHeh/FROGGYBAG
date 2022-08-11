from django.contrib import admin
from apps.blog.models import Article, BlogCategory, Tag
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

# admin.site.register(Article)
# admin.site.register(BlogCategory)
admin.site.register(Tag)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'artticle_list_link']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image_tag', 'image']
    readonly_fields = ['image_tag']

    def artticle_list_link(self, obj):
        count = Article.objects.filter(category=obj).count()
        url = (
            reverse('admin:blog_article_changelist')
            + '?'
            + urlencode({'category__id': obj.id, 'category__id__exact': obj.id})
        )
        return format_html(f"<a href='{url}'>Статьи(ей): {count}</a>")

    artticle_list_link.short_description = 'Статьи'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag_thumbnail', 'category_link', 'created_at', 'tags_links']
    list_display_links = ['id', 'title', 'image_tag_thumbnail']
    fields = ['category', 'user', 'image_tag', 'image', 'tags', 'title', 'text_preview', 'text']
    readonly_fields = ['image_tag']
    list_filter = ['category']

    def category_link(self, obj):
        if obj.category:
            url = reverse('admin:blog_blogcategory_change', args=[obj.category.id])
            return format_html(f"<a href='{url}'>{obj.category.name}</a>")

    category_link.short_description = 'Категория'

    def tags_links(self, obj):
        tags = obj.tags.all()
        html_tag = ''
        for tag in tags:
            url = reverse('admin:blog_tag_change', args=[tag.id])
            html_tag = html_tag + f", <a href='{url}'>{tag.name}</a>"
        return format_html(html_tag[2:])

    tags_links.short_description = 'Тэги'
