from django.db import models
from django.db.models.fields import CharField

class Home(models.Model):
    titulo=models.CharField('Título', max_length=30)
    subtitulo=models.CharField('Subtítulo', max_length=50)
    imagem=models.ImageField('Imagem', upload_to='imagemhome/', null=True, blank=True)

class Sobre(models.Model):
    descricao=models.TextField('Descrição')

class Servico(models.Model):
    descricaoupload=models.TextField('Descrição do upload')
    descricaovideo=models.TextField('Descrição de assistir')

class Depoimentos(models.Model):
    imagem_depoimento=models.ImageField('Imagem do depoimento', upload_to='imagemdepoimento/', null=True, blank=True)
    nome_depoimento=models.CharField('Nome do depoimento', max_length=20, blank=True)
    depoimento=models.TextField('Depoimento', blank=True)

class Assist(models.Model):
    titulo_video=models.CharField('Título do vídeo', max_length=30)

class Contato(models.Model):
    email=models.EmailField('Email')
    numero=models.CharField('Número', max_length=10)
    