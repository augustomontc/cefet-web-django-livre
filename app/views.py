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

# Create your views here.LoginRequiredMixin
class ListarPasteis(ListView):
    model = Pastel
    template_name = 'listar_pasteis.html'

class RemoverPastel(DeleteView):
    model = Pastel
    template_name = 'deletar_pastel.html'
    success_url = reverse_lazy('listar_pasteis')

class SalvarPastel():
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
class ListarRecheios(ListView):
    model = Recheio
    template_name = 'listar_recheios.html'

    def get_queryset(self):
        return Recheio.objects.annotate(valor_total=ExpressionWrapper(F('quantidade')*F('preco'),\
                            output_field=DecimalField(max_digits=10,\
                                                    decimal_places=2,\
                                                     blank=True)\
                                                    )\
                            )

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class RemoverRecheio(DeleteView):
    model = Recheio
    template_name = 'deletar_recheio.html'
    success_url = reverse_lazy('listar_recheios')

class SalvarRecheio():
    model = Recheio
    fields = ['nome','quantidade','preco','img_recheio']
    template_name = 'salvar_recheio.html'
    success_url = reverse_lazy('listar_recheios')

class InserirRecheio(SalvarRecheio,CreateView):
    pass

class AtualizarRecheio(SalvarRecheio,UpdateView):
    pass