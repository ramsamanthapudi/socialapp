from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from braces.views import SelectRelatedMixin
from django.http import Http404
from .models import Post
from . import forms
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin,LoginRequiredMixin,ListView):
    model = Post
    select_related = ('user', 'group')

class UserPosts(ListView):
    model = Post
    template_name = 'posts/user_posts_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
             raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user']=self.post_user
        return context

class PostDetail(SelectRelatedMixin,LoginRequiredMixin,DetailView):
    model = Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    model = Post
    fields = ('message','group')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user= self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model = Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

