from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import PerfilUsuario


class Perfil(DetailView):
    model= PerfilUsuario
    template_name = 'usuario/perfil.html'


class EditarPerfil(UpdateView):
    model= PerfilUsuario
    fields = ['nombre', 'apellido', 'dni', 'photo']
    template_name = 'usuario/editarPerfil.html'
    success_url = reverse_lazy('perfil_lista')


class NuevoPerfil(CreateView):
    model= PerfilUsuario
    template_name = 'usuario/NuevoPerfil.html'
    fields = ['nombre', 'apellido', 'dni', 'photo']
    success_url = reverse_lazy('perfil_lista')


class BorrarPerfil(DeleteView):
    model= PerfilUsuario
    template_name = 'usuario/borrarPerfil.html'
    success_url = reverse_lazy('perfil_lista')

class ListaPerfil(ListView):
    model= PerfilUsuario
    template_name = 'usuario/lista.html'
    
