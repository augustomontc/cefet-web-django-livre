"""tp2 URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url
from app import views

urlpatterns = [
    path('pastel', views.ListarPasteis.as_view(), name='listar_pasteis'),
    path('pastel/novo', views.InserirPastel.as_view(), name='criar_pastel'),
    path('pastel/editar/<int:pk>', views.AtualizarPastel.as_view(), name='editar_pastel'),
    path('pastel/deletar/<int:pk>', views.RemoverPastel.as_view(), name='deletar_pastel'),
    path('recheio', views.ListarRecheios.as_view(), name='listar_recheios'),
    path('recheio/novo', views.InserirRecheio.as_view(), name='criar_recheio'),
    path('recheio/editar/<int:pk>', views.AtualizarRecheio.as_view(), name='editar_recheio'),
    path('recheio/deletar/<int:pk>', views.RemoverRecheio.as_view(), name='deletar_recheio'),
    #path('login',LoginView.as_view(template_name="login.html"),name="login"),
    #path('logout',LogoutView.as_view(next_page="/login"),name="logout"),
]
