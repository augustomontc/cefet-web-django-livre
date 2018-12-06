from django.contrib import admin
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Pastel(models.Model):
	farinha = models.CharField(max_length=45)
	recheio = models.ManyToManyField('Recheio')

	def __str__(self):
		return u'{0} com {1}'.format(self.farinha,self.recheio)

class Recheio(models.Model):
	nome = models.CharField(max_length=45)
	preco = models.DecimalField(max_digits=10,decimal_places=2)
	img_recheio = models.ImageField(upload_to="imgs",verbose_name="Imagem")

	def __str__(self):
		return self.nome

@admin.register(Recheio)
class RecheioAdmin(admin.ModelAdmin):
    pass