from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

class ArticleInLine(admin.TabularInline):
    model = models.About
    extra = 0


# Register your models here.

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('presentation','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('presentation',)
    date_hierarchy = 'date_add'
    list_display_links = ['presentation',]
    ordering = ['presentation',]
    list_per_page = 10

@admin.register(models.SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('logo','slogan','description','contact','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('slogan',)
    date_hierarchy = 'date_add'
    list_display_links = ['slogan',]
    ordering = ['slogan',]
    list_per_page = 10
