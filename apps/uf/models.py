from django.db import models

# Create your models here.

class Home(models.Model):
	titulo = models.CharField(verbose_name='Título', max_length=30)
    texto = models.CharField(verbose_name='Subtítulo', max_length=50)
    imagem = models.ImageField(verbose_name='Imagem', upload_to= "imagenshome", blank=True, null=True)


class Servico(models.Model):
	titulo = models.Charfield(verbose_name='Título', max_length=30)