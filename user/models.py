from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"