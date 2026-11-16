from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=80, null=False)
    nacionalidad = models.CharField(max_length=80, null=False)
    anio_nacimiento = models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name_plural = "Autores"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.anio_nacimiento}"

class Libro(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    isbn = models.CharField(max_length=100, unique= True, null=False)
    anio_publicacion = models.PositiveIntegerField(null=False)

    autor_id = models.ForeignKey(Autor, related_name='autor_id', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Libros"

    def __str__(self):
        return f"{self.titulo} {self.anio_publicacion} {self.autor_id}"









