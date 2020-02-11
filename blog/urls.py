from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('single', views.single, name='single'),
    path('archive', views.archive, name='archive'),
    path('video', views.video, name='video'),
    

]
