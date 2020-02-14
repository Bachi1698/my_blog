from django.shortcuts import render
from .import models  # importation de fichier models.py (fichier contenant tous nos models)
from about import models as about_model
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request): 
    article = models.Article.objects.filter(status=True) # récupération des articles qui ont pour status true
    article_recent = models.Article.objects.all().order_by('-date_add')[:3] # récupération des trois articles les plus récente
    article_vue = models.Article.objects.order_by('-vue')[:3] # récupération des trois articles les plus vue
    categorie = models.Categorie.objects.filter(status=True) # récuperation des categorie avec status True
    article_v = models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo
    article_r = models.Article.objects.order_by('-date_add')[:1]
    site_info = about_model.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    print(request.user)
    datas = {
        'article_recent': article_recent,
        'article_vue': article_vue,
        'article': article,
        'site_info': site_info,
        'article_v': article_v,
        'categorie': categorie,
        'article_r': article_r,
       
    }
    return render(request, "pages/index.html", datas)

def video(request):
    site_info = about_model.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    article_v = models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo

    datas = {
        'site_info': site_info,
    }
    return render(request, "pages/video-post.html",datas)

@login_required(login_url='login')
def single(request, pk):
    site_info = about_model.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    article = models.Article.objects.get(pk=pk) # permet de recuperer l'article
    commentaire = models.Commentaire.objects.filter(article__pk=pk) # permet de recuperer les commentaires d'un article
    article_v = models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo
    datas = {
       'article':article,
       'commentaire':commentaire,
       'article_v':article_v,
       'site_info': site_info,
    }
    return render(request, "pages/single-post.html",datas)

def archive(request):
    site_info = about_model.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    article = models.Article.objects.filter(status=True)
    article_v = models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo
    # categorie = models.Categorie.objects.filter(status=True)
    datas = {
        # 'categorie':categorie,
        'article': article,
        'site_info': site_info,
        'article_v':article_v,
    }
    return render(request, "pages/archive-grid.html",datas)

def recherche(request):
    result = True
    if request.method == "POST":
        mot_r = request.POST.get("recherche")
        print(mot_r)
        recherche_count = models.Article.objects.filter(titre__icontains=mot_r).count()
        recherche = models.Article.objects.filter(titre__icontains=mot_r)
        print(recherche)
        if recherche_count == 0:
            result = False
    site_info = about_model.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    article = models.Article.objects.filter(status=True)
    article_v = models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo
    # categorie = models.Categorie.objects.filter(status=True)
    datas = {
        'result':result,
        'recherche': recherche,
        'site_info': site_info,
        'article_v':article_v,
    }
    return render(request, "pages/recherche.html",datas)



