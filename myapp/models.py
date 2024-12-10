from django.db import models

# Create your models here.
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
