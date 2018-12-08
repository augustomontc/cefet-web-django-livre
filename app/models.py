from django.contrib import admin
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Pastel(models.Model):
	Normal = "Normal"
	Integral = "Integral"
	FARINHA_CHOICES = (
		(None, "Escolha..."),
		(Normal,Normal),
		(Integral,Integral),
	)
	nome = models.CharField(max_length=45)
	farinha = models.CharField(max_length=45, choices=FARINHA_CHOICES)
	recheio = models.CharField(max_length=45)

	def __str__(self):
		return u'{0} de farinha {1} recheado com {2}'.format(self.nome,self.farinha,self.recheio)

	def get_img_recheio(self):
		obj_recheio = Recheio.objects.get(nome=self.recheio)
		return obj_recheio.img_recheio

class Recheio(models.Model):
	nome = models.CharField(max_length=45, unique=True)
	preco = models.DecimalField(max_digits=10,decimal_places=2)
	img_recheio = models.ImageField(upload_to="imgs",verbose_name="Imagem")

	def __str__(self):
		return self.nome

@admin.register(Recheio)
class RecheioAdmin(admin.ModelAdmin):
    pass