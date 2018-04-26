"""VisualizationProject URL Configuration

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
# from django.contrib import admin
import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^top_ten_taxons/', views.top_ten_taxons),
    # url(r'^home/', views.home),
    # url(r'^trade_country_map/', views.trade_country_map),
    # url(r'^map_live/', views.map_live),
    # url(r'^map_import/', views.map_import),
    # url(r'^map_export/', views.map_export),
    url(r'^load_live_map/', views.load_live_map),
    url(r'^load_export_map/', views.load_export_map),
    url(r'^load_import_map/', views.load_import_map),
]
