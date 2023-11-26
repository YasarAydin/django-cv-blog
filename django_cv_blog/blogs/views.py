from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    blogs = models.Article.objects.filter(is_active=True).order_by("-created_date")
    return render(request, "index.html", context={
        "blogs": blogs
    })


def blog_detail(request, slug):
    blog = models.Article.objects.get(slug=slug)
    return render(request, "blog-details.html", context={
        "blog": blog
    })


def kategoriler(request):
    categories = models.Category.objects.all()
    return render(request, "category.html", context={
        "categories": categories
    })


def kategoriler_detay(request, slug):
    category = models.Category.objects.get(slug=slug)
    blogs = models.Article.objects.filter(categories=category)
    return render(request, "index.html", context={
        "blogs": blogs
    })
