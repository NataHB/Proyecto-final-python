from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    seleccion = (
        ('Pasteleria', 'Pasteleria'),
        ('Bebidas', 'bebidas'),
    )
    categoria = models.CharField(max_length=40, choices=seleccion)
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    titulo = models.CharField(max_length=40, default='Sin título')
    descripcion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return ( f'{self.nombre}' ) 

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.ForeignKey(User, on_delete=models.CASCADE )
    mensaje = models.TextField(null=True, blank=True)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return ( f'{self.nombre} - {self.producto}' )
