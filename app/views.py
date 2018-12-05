from django.shortcuts import render
from django.db.models import F,ExpressionWrapper,DecimalField
from django.http import HttpResponseRedirect
from django.views import View
from django.forms import ModelForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pastel

# Create your views here.
class ListarPasteis(LoginRequiredMixin,ListView):
    model = Pastel
    template_name = 'listar_pasteis.html'

class RemoverPastel(LoginRequiredMixin,DeleteView):
    model = Pastel
    template_name = 'deletar_pastel.html'
    success_url = reverse_lazy('listar_pasteis')

class SalvarPastel(LoginRequiredMixin):
    model = Pastel
    fields = ['farinha','recheio']
    template_name = 'salvar_pastel.html'
    success_url = reverse_lazy('listar_pasteis')

class InserirPastel(SalvarPastel,CreateView):
    pass

class AtualizarPastel(SalvarPastel,UpdateView):
    pass