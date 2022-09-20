from django.contrib import admin

from . import models
# Register your models here.

class StackedInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        StackedInline,
    ]

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)