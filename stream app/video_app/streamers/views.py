from django.shortcuts import render, redirect, get_object_or_404
from . models import VidStream
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 

class VideoCreateView(LoginRequiredMixin   ,CreateView):
    model = VidStream
    success_url = "/"
    template_name = 'stream/post-video.html'
    fields = ['title', 'description','video']


    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.streamer = self.request.user 
        return super().form_valid(form)

class GeneralVideoListView(ListView):
    model = VidStream
    template_name = 'stream/video-list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']
    
class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = VidStream
    template_name = 'stream/post-video.html'
    success_url = "/"
    fields = ['title','description','video']


    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.streamer = self.request.user 
        return super().form_valid(form)
    #this function prevents other people from updating your videos
    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False