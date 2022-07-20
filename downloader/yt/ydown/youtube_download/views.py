from ast import Return
from django.shortcuts import render
# pytube package for download youtube video
from pytube import YouTube

def ytb_down(request):
    return render(request, 'ytb_main.html')

def yt_download(request):
    url = request.GET.get('url')
    obj = YouTube(url)
    resolutions = []
    strm_all = obj.streams.all()
    for i in strm_all:
        resolutions.append(i.resolution)
    resolutions = list(dict.fromkeys(resolutions))

    embed_link = url.replace("watch?v=", "embed/")
    return render(request, 'yt_download.html', {'rsl': resolutions, 'embd': embed_link})