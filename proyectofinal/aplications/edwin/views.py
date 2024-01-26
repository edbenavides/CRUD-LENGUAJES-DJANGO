from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from.models import BDInmueble
from.forms import ActivosForm

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

#class ProyectoView(TemplateView):
    #template_name = "home.html"

class HomeView(TemplateView):
    template_name = "home.html"



class ProyectoCreateView(CreateView):
    model = BDInmueble
    template_name = "inmuebles.html"
    forms_class = ActivosForm
    fields = ['nombre_edificio','apartamento','habitaciones','propietario','banos']
    success_url= "/crear"

class ProyectoListView(ListView):
    model = BDInmueble
    template_name = "listar.html"
    context_object_name ="datos"

class ProyectoActualizarListView(ListView):
    model = BDInmueble
    template_name = "listar_actualizar.html"
    context_object_name ="datos"

class ProyectoUpdateView(UpdateView):
    model = BDInmueble
    template_name = "actualizar.html"
    fields = ['nombre_edificio','apartamento','habitaciones','propietario','banos']
    context_object_name = 'datos'
    success_url = 'proyectolistar_actualizar'
    def get_success_url(self):
        return reverse('proyectolistar_actualizar')

class ProyectoEliminarListView(ListView):
    model = BDInmueble
    template_name = "listar_eliminar.html"
    context_object_name ="datos"

class ProyectoDeleteView(DeleteView):
    model = BDInmueble
    template_name = "eliminar.html"
    context_object_name ="datos"
    success_url = 'proyectolistar_eliminar'
    def get_success_url (self):
        return reverse('proyectolistar_eliminar')