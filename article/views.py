from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

from .models import Post


class PostListing(ListView):
    model = Post


class PostCreate(CreateView):
    model = Post
    success_url = '/'
    fields = '__all__'


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk, })


class PostDelete(DeleteView):
    model = Post
    success_url = '/'
