"""
URL configuration for disciplines project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponse


def read_file(request):
    f = open('.well-known/pki-validation/13B8529046B09404DE91BBE7E0BCD134.txt','r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content,content_type = "text/plain")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('discipline.urls')),
    path("comments/", include('comments.urls'),),
    path('.well-known/pki-validation/13B8529046B09404DE91BBE7E0BCD134.txt',read_file),
]
