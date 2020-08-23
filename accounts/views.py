from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from . forms import UserChereForm
from django.urls import reverse_lazy
# Create your views here.
class UserChereView(CreateView):
    template_name = 'accounts/Cheru.html'
    form_class = UserChereForm
    success_url = reverse_lazy('login') # reverse lazy will wait till the signup activity completes


class Diksoochi(TemplateView):
    template_name = 'accounts/index.html'


class loginview(TemplateView):
    template_name = 'accounts/login.html'


class logoutview(TemplateView):
    template_name = 'accounts/logout.html'