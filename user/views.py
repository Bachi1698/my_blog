from django.shortcuts import render, redirect
from . import forms 
from about import models as about_models
# Create your views here.


def inscription(request):
    form=""
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.RegistrationForm()
    
    site_info = about_models.SiteInfo.objects.filter(status=True)[:1].get() # permet de recuperer les infos
    datas = {
        'form':form,
        'site_info':site_info
        
    }
    return render(request, "registration/inscription.html", datas)

