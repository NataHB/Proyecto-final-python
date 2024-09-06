from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from mi_app.models import Producto, Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


#VISTAS SIN LOGIN
class HomeView(TemplateView):
    template_name = 'mi_app/index.html'

class AboutView(TemplateView):
    template_name = 'mi_app/about.html'

# PASTELERIA
class PasteleriaView(LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = 'pasteleria'
    template_name = 'mi_app/pasteleria_list.html'

class PasteleriaDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'pasteleria'
    template_name = 'mi_app/pasteleria_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()  # Filtra comentarios por producto
        return context

class PasteleriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'mi_app/pasteleria_confirm_delete.html'
    success_url = reverse_lazy('pasteleria')


# BEBIDAS
class BebidaView(LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = 'bebidas'
    template_name = 'mi_app/bebidas_list.html'

class BebidaDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'bebidas'
    template_name = 'mi_app/bebidas_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()  # Filtra comentarios por producto
        return context

class BebidaDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'mi_app/bebidas_confirm_delete.html'
    success_url = reverse_lazy('bebidas')

# PRODUCTOS (PASTELERIA Y BEBIDAS)
class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['categoria', 'nombre', 'imagen', 'titulo', 'descripcion', 'precio']
    template_name = 'mi_app/productoNuevo.html'
    success_url = reverse_lazy('productoNuevo')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['categoria', 'nombre', 'imagen', 'titulo', 'descripcion', 'precio']
    template_name = 'mi_app/producto_update.html'
    success_url = reverse_lazy('index')

# COMENTARIOS
class ComentariosCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ['nombre', 'comentario', 'mensaje']
    template_name = 'mi_app/comentario.html'

    def form_valid(self, form):
        form.instance.pasteleria_id = self.kwargs['pk']  # Vincula el comentario con la pasteleria/producto
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')
