from django.shortcuts import render

# Create your views here.


def inscription(request):
    datas = {
    }
    return render(request, "registration/inscription.html", datas)

