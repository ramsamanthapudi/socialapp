from django.urls import path
from .views import UserChereView, Diksoochi
from django.contrib.auth import views

app_name='accounts'
urlpatterns = [
    path('CHeru/', UserChereView.as_view(), name='cheru'),
    path('diksoochi/', Diksoochi.as_view(), name='diksoochi'),
    path('login/', views.LoginView.as_view(template_name='accounts/login.html',redirect_field_name='accounts/index.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
