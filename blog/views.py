from django.shortcuts import render

# Create your views here.

def home(request):
    datas = {
        
    }
    return render(request, "pages/index.html", datas)

def video(request):
    datas = {
        
    }
    return render(request, "pages/video-post.html",datas)

def single(request):
    datas = {
        
    }
    return render(request, "pages/single-post.html",datas)

def archive(request):
    datas = {
        
    }
    return render(request, "pages/archive-grid.html",datas)



