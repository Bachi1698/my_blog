from django.shortcuts import render
from .import models
from about import models as about_model

# Create your views here.
def contact(request):
    site_info = about_model.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    article_v = models.Article.objects.exclude(video=None) # récupération des articles ayant des vidéo
    datas = {
        'site_info': site_info,
        'article_v':article_v,
    }
    return render(request, "pages/contact.html", datas)
