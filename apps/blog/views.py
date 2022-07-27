from django.shortcuts import render

from apps.blog.models import BlogCategory, Article, Tag


def blog_category_list(request):
    print(request)
    blog_categories = BlogCategory.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/category/list.html', {'categories': blog_categories, 'tags': tags})


def category_article_list(request, category_id):
    print(request)
    articles = Article.objects.filter(category=category_id)
    return render(request, 'blog/article/list.html', {'articles': articles})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/view.html', {'article': article, 'category': category})


def tag_article_list(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags__name=tag)
    return render(request, 'blog/tag/tag_filter_list.html', {'articles': articles})
