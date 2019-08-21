from django.contrib import admin

from .models import Article, Category, ArticleByCategory


class ArticleByCategoryInline(admin.TabularInline):

    model = ArticleByCategory
    extra = 1

class ArticleAdmin(admin.ModelAdmin):

    inlines = [ArticleByCategoryInline]

class CategoryAdmin(admin.ModelAdmin):

    inlines = [ArticleByCategoryInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

