from django.db import models

# Create your models here.
class Categorie(models.Model):
    
    nom = models.CharField( max_length=250)
    description = models.TextField()
    image = models.ImageField( upload_to='images/categories')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __init__(self):
        return self.nom
    
    class Meta:
        verbose_name="Catgégorie"
        verbose_name_plural="Catgégories"
        
        
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
    titre = models.CharField( max_length=50)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        pass
