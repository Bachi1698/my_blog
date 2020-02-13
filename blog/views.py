from django.shortcuts import render
from .import models  # importation de fichier models.py (fichier contenant tous nos models)
# Create your views here.

def home(request): 
    article = models.Article.objects.filter(status=True) # récupération des articles qui ont pour status true
    article_recent = models.Article.objects.order_by('-date_add')[:3] # récupération des trois articles les plus récente
    article_vue = models.Article.objects.order_by('-vue')[:3] # récupération des trois articles les plus vue
    categorie = models.Categorie.objects.filter(status=True) # récuperation des categorie avec status True
    article_v = models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo
    print(request.user)
    datas = {
        'article_recent': article_recent,
        'article_vue': article_vue,
        'article': article,
        'article_v': article_v,
        'categorie': categorie,
    }
    return render(request, "pages/index.html", datas)

def video(request):
    datas = {
        
    }
    return render(request, "pages/video-post.html",datas)

def single(request):
    datas = {
        
    }
    return render(request, "pages/single-post.html",datas)

def archive(request):
    article = models.Article.objects.filter(status=True)
    # categorie = models.Categorie.objects.filter(status=True)
    datas = {
        # 'categorie':categorie,
        'article': article,
    }
    return render(request, "pages/archive-grid.html",datas)



