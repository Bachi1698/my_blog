from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','status', 'view_image')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url = obj.image.url ))


@admin.register(models.Tague)
class TagueAdmin(admin.ModelAdmin):
    list_display = ('nom','status')



