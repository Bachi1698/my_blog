from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


class ArticleInLine(admin.TabularInline):
    model = models.Article
    extra = 0


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','status','date_add', 'date_update' ,'view_image' )
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    inlines = [
        ArticleInLine
    ]
    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url = obj.image.url ))


@admin.register(models.Tague)
class TagueAdmin(admin.ModelAdmin):
    list_display = ('nom','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('categorie','auteur','titre','status','vue','date_add', 'date_update','view_image','view_video')
    list_filter = ('status','categorie','auteur')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['categorie','auteur','titre',]
    ordering = ['titre',]
    list_per_page = 10  
    filter_horizontal = ('tague',)
    # readonly_fields = ['view_image', 'view_video']
    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="120px" height="150px" />'.format(url = obj.image.url ))
    def view_video(self, obj):
        return mark_safe('<iframe src="https://www.youtube.com/embed/1nI-GMmHMHs" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'.format(url = obj.video ))


@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('user','article','like','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('user',)
    date_hierarchy = 'date_add'
    list_display_links = ['user','article']
    ordering = ['date_add',] 
    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="120px" height="150px" />'.format(url = obj.image.url ))
    
    
@admin.register(models.ReponseCommentaire)
class ReponseCommentaireAdmin(admin.ModelAdmin):
    list_display = ('user','commentaire','status','date_add', 'date_update')
    list_filter = ('status',)
    search_fields = ('user',)
    date_hierarchy = 'date_add'
    list_display_links = ['user',]
    ordering = ['date_add',] 
    def view_image(self, obj): 
        return mark_safe('<img src="{url}" width="120px" height="150px" />'.format(url = obj.image.url ))




