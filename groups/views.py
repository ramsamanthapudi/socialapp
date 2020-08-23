from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from groups.models import Group
# Create your views here.
class CreateGroup(LoginRequiredMixin,CreateView):
    model = Group
    fields = ('name','description','image')

class GroupDetail(DetailView):
    model = Group

class GroupList(ListView):
    model = Group
