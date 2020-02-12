from django.db import models

# Create your models here.

class About(models.Model):
    presentation = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'
        
    def __str__(self):
        return "site-info"
    
class SiteInfo(models.Model):
    logo = models.ImageField(upload_to='image/logo')
    slogan = models.CharField(max_length=50)
    description = models.TextField()
    contact = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'siteinfo'
        verbose_name_plural = 'siteinfos'
        
    def __str__(self):
        return self.slogan
    
    
    
