from django.contrib import admin
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Pastel(models.Model):
	nome = models.CharField(max_length=45, default='Pastelao')
	farinha = models.CharField(max_length=45)
	recheio = models.CharField(max_length=45, default='Carne')
	#recheio = models.ManyToManyField('Recheio')

	def __str__(self):
		return u'{0} de {1} com {2}'.format(self.nome,self.farinha,self.recheio)

class Recheio(models.Model):
	nome = models.CharField(max_length=45)
	preco = models.DecimalField(max_digits=10,decimal_places=2)
	img_recheio = models.ImageField(upload_to="imgs",verbose_name="Imagem")

	def __str__(self):
		return self.nome

@admin.register(Recheio)
class RecheioAdmin(admin.ModelAdmin):
    pass