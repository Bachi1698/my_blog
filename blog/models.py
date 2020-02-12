from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    
    nom = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/categories')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.nom
        
class Tague(models.Model):
    """Model definition for Tague."""
    nom = models.CharField( max_length=250)
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Tague."""

        verbose_name = 'Tague'
        verbose_name_plural = 'Tagues'

    def __str__(self):
        """Unicode representation of Tague."""
        return self.nom

class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    titre = models.CharField( max_length=250)
    image = models.ImageField(upload_to='image/article')
    video = models.URLField(max_length=255)
    description = models.TextField()
    tague = models.ManyToManyField(Tague)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='article_categorie')
    vue = models.IntegerField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteur_article')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre
    
class Commentaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_commentaire')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='article_commentaire')
    message = models.TextField()
    like = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = 'commentaires'
        
    def __str__(self):
        return self.user.username
    
class ReponseCommentaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_reponse')
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE,related_name='reponse_commentaire')
    message = models.TextField()
    like = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'ReponseCommentaire' 
        verbose_name_plural ='ReponsesCommentaire'    
        
        def __str__(self):
            return self.user.username