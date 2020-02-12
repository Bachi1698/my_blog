from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','nom','sujet','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    
@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    list_display_links = ['email',]
    ordering = ['email',]
    