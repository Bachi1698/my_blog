from django.shortcuts import render

# Create your views here.
def login(request):
    datas = {
    }
    return render(request, "pages/login.html", datas)

def inscription(request):
    datas = {
    }
    return render(request, "pages/inscription.html", datas)

