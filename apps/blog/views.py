from django.shortcuts import render
from django.urls import reverse

from apps.blog.models import BlogCategory, Article, Tag
from config.settings import PAGE_NAMES


def blog_category_list(request):
    print(request)
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    tags = Tag.objects.all()
    return render(request, 'blog/category/list.html',
                  {'categories': blog_categories, 'tags': tags, 'breadcrumbs': breadcrumbs})


def category_article_list(request, category_id):
    print(request)
    articles = Article.objects.filter(category=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog'], 'current': category.name}
    return render(request, 'blog/article/list.html', {'articles': articles, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog'],
                   reverse('category_article_list', args=[category.id]): category.name,
                   'current': article.title}
    return render(request, 'blog/article/view.html',
                  {'article': article, 'category': category, 'breadcrumbs': breadcrumbs})


def tag_article_list(request, tag_id):
    searched_tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags__name=searched_tag)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog'],
                   'current': searched_tag.name}
    return render(request, 'blog/tag/tag_filter_list.html',
                  {'articles': articles, 'searched_tag': searched_tag,
                   'breadcrumbs': breadcrumbs})
