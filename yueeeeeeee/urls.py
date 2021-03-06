"""yueeeeeeee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from yueeeeeeee.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', RedirectView.as_view(url='http://yueeeeeeee.com/blog'), name='redirect to index'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('image/', include('image.urls', namespace='image')),
    path('account/', include('account.urls', namespace='account')),
    path('social_auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)