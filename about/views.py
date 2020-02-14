from django.shortcuts import render
from .import models
from blog import models as blog_models
# Create your views here.
def about(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    article_v = blog_models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo
    datas = {
        'site_info': site_info,
        'article_v':article_v,
    }
    return render(request, "pages/about.html", datas)
