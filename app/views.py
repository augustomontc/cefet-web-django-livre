from django.shortcuts import render
from django import forms
from django.db.models import F,ExpressionWrapper,DecimalField
from django.http import HttpResponseRedirect
from django.views import View
from django.forms import ModelForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pastel, Recheio
from app.forms import PastelForm
from django.views.generic.edit import FormView

'''
    Pasteis
'''
class ListarPasteis(LoginRequiredMixin,ListView):
    model = Pastel
    template_name = 'listar_pasteis.html'

class RemoverPastel(LoginRequiredMixin,DeleteView):
    model = Pastel
    template_name = 'deletar_pastel.html'
    success_url = reverse_lazy('listar_pasteis')

class SalvarPastel(LoginRequiredMixin):
    model = Pastel
    form_class = PastelForm
    template_name = 'salvar_pastel.html'
    success_url = reverse_lazy('listar_pasteis')

    def form_invalid(self, form):
        return http.HttpResponse("form is invalid..")


class InserirPastel(SalvarPastel,CreateView):
    pass

class AtualizarPastel(SalvarPastel,UpdateView):
    pass

'''
    Recheios
'''
class ListarRecheios(LoginRequiredMixin, ListView):
    model = Recheio
    template_name = 'listar_recheios.html'

class RemoverRecheio(LoginRequiredMixin,DeleteView):
    model = Recheio
    template_name = 'deletar_recheio.html'
    success_url = reverse_lazy('listar_recheios')

class SalvarRecheio(LoginRequiredMixin):
    model = Recheio
    fields = ['nome','preco','img_recheio']
    template_name = 'salvar_recheio.html'
    success_url = reverse_lazy('listar_recheios')

class InserirRecheio(SalvarRecheio,CreateView):
    pass

class AtualizarRecheio(SalvarRecheio,UpdateView):
    pass