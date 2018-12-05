from django.contrib import admin
from django.db import models

# Create your models here.
class Pastel(models.Model):
	farinha = models.CharField(max_length=45)
	recheio = models.ManyToManyField('Recheio')

class Recheio(models.Model):
	nome = models.CharField(max_length=45)
	quantidade = models.IntegerField()
	preco = models.DecimalField(max_digits=10,decimal_places=2)
	img_recheio = models.ImageField(upload_to="imgs",verbose_name="Imagem")

	def __str__(self):
		return self.quantidade + " porções de " + self.nome

@admin.register(Recheio)
class RecheioAdmin(admin.ModelAdmin):
    pass