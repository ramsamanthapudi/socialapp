"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import urls as us
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from groups import urls as us1
from posts import urls as us2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(us)),
    path('thanks/', views.logoutview.as_view(), name='thanks'),
    path('groups/',include(us1)),
    path('posts/',include(us2))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
