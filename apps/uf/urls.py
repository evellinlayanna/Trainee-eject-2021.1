from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('servicos', views.servicos, name='servicos'),
    path('upload', views.upload, name='upload'),
    path('assist', views.assist, name='assist'),
    path('explorar', views.explorar, name='explorar'),
    path('contato', views.contato, name='contato'),
    path('notfound', views.notfound, name='notfound'),
]