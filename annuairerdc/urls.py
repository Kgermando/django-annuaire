"""annuairerdc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from persons import views
from persons.views import SearchView
from django.views.generic import TemplateView

urlpatterns = [
    url('admin/', admin.site.urls, name='admin'),
    # url(r'^$', TemplateView.as_view(template_name="pages/index.html"), name='home'),
    url(r'^contact/$', TemplateView.as_view(template_name="pages/contact.html"), name='contact'),
    url(r'^$', SearchView.as_view(), name='search'),
    url(r'^search/detail/(?P<id>[0-9]+)$', views.detail, name='details'),
    # url(r'^accounts/', include('allauth.urls'), name='allauth'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
