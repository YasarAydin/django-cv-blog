from django.contrib import admin
from . import models


# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    readonly_fields = ["slug"]


admin.site.register(models.Category, CategoryModelAdmin)


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    readonly_fields = ["slug"]
    search_fields = ["title"]


admin.site.register(models.Article, ArticleModelAdmin)
