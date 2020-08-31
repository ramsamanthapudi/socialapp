from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from groups.models import Group, GroupMember
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
class CreateGroup(LoginRequiredMixin,CreateView):
    model = Group
    fields = ('name','description','image')

class GroupDetail(DetailView):
    model = Group

class GroupList(ListView):
    model = Group

# class JoinGroup(LoginRequiredMixin,RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('groups:detail', kwargs={'pk':self.pk})
#
#     def get(self, request, *args, **kwargs):
#         group = get_object_or_404(Group,kwargs={'pk':self.pk})
#
#         try:
#             GroupMember.objects.create(user=self.request.user,group=group)
#         except :
#             messages.warning(self.request,'You are already a member of this group')
#         else:
#             messages.success(self.request,'you are now a member')
#
#         return super().get(request, *args, **kwargs)
#
# class LeaveGroup(LoginRequiredMixin,RedirectView):
#
#     def get(self, request, *args, **kwargs):
#         group = get_object_or_404(Group,kwargs={'pk':self.pk})
#
#         try:
#             membership = GroupMember.objects.filter(
#                 user= self.request.user#,
#                 #group__slug=self.kwargs.get('slug')
#             ).get()
#         except:
#             messages.warning(self.request, 'You are not in this group')
#         else:
#             membership.delete()
#             messages.success(self.request,'You left the group successfully')
#         return super().get(request,*self,**kwargs)