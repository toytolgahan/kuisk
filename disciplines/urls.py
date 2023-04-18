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
from django.urls import path, include, re_path
from django.contrib.staticfiles.views import serve
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('discipline.urls')),
    path("comments/", include('comments.urls')),
    re_path(r'^\.well-known/(?P<path>.*)$', serve, kwargs={'document_root': str(settings.BASE_DIR / '.well-known')}),

]
