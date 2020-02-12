from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('adresse','contact','user','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('user',)
    date_hierarchy = 'date_add'
    list_display_links = ['adresse','contact',]
    ordering = ['user',]
    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url = obj.image.url ))