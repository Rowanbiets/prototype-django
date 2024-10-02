from django.contrib import admin
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","content","author","created_at","source",)

admin.site.register(Article, ArticleAdmin)
