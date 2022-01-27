"""esoft1 URL Configuration

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
from esoftapi.views import view_index, view_login, view_home, view_produtos

urlpatterns = [
    path('', view_index.index),
    path('login/', view_login.login),
    path('autenticar', view_login.autenticar),
    path('cadastro/', view_login.cadastro),
    path('salvar_cadastro', view_login.salvar_cadastro),
    path('logout/', view_login.logout),
    path('home/', view_home.home),
    path('produtos/', view_produtos.produtos),
    path('salvar_produto', view_produtos.salvar_produto),
    path('get_produto/', view_produtos.get_produto),
    path('del_produto/', view_produtos.del_produto),
    path('admin/', admin.site.urls),
   
]
