from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField( max_length=254)
    nom = models.CharField(max_length=250)
    sujet = models.CharField( max_length=50)
    message = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        
    def __str__(self):
        return self.nom
    
    
class Newsletter(models.Model):
    email = models.EmailField( max_length=254)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'
        
    def __str__(self):
        return self.email