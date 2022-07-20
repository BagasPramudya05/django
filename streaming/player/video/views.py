from django.shortcuts import render
from .models import video

def index(request):
    if request.method=="GET":
        da=video.objects.all()
        return render(request,'index.html',{'da':da})
