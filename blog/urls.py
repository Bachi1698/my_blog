from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('single/<int:pk>', views.single, name='single'), #permet de dynamiser la vue en fonction d'un article
    path('archive', views.archive, name='archive'),
    path('video', views.video, name='video'),
    
    

]
