from django.contrib import admin
from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'description', 'category')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)