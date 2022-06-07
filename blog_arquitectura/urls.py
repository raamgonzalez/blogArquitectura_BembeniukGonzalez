"""blog_arquitectura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from blog_arquitectura.views import index
from app_blog.views import obras_arq_view, inst_edu_view, bibliografia_view, cargar_obra, cargar_Instedu, cargar_bibliografia,search_obra

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('obras_arq_view/', obras_arq_view,name='obras_arq_view'),
    path('inst_edu_view/', inst_edu_view,name='inst_edu_view'),
    path('bibliografia_view/', bibliografia_view,name='bibliografia_view'),
    path('obras_arq_view/cargar_obra/', cargar_obra,name='cargar_obra'),
    path('inst_edu_view/cargar_Instedu/', cargar_Instedu ,name='cargar_Instedu'),
    path('bibliografia_view/cargar_bibliografia/', cargar_bibliografia ,name='cargar_bibliografia'),
    path('obras_arq_view/search_obra/', search_obra ,name='search_obra'),
]
