from django.db import models
import os


class Album(models.Model):
    name = models.CharField(verbose_name="Título", max_length=200)
    cover = models.ImageField(verbose_name="Portada", upload_to='gallery', default='gallery/no-img.jpg')

    class Meta:
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'
        ordering = ['name']
    
    def __str__(self):
        #return "[" + str(self.id) + "] " + self.name
        return self.name

class Image(models.Model):
    image = models.ImageField(verbose_name="Archivo", upload_to='gallery', default='gallery/no-img.jpg')
    name = models.CharField(verbose_name="Título", max_length=200)
    details = models.CharField(verbose_name="Materiales/Técnica", max_length=200)
    size = models.CharField(verbose_name="Dimensiones", max_length=200)
    disp = models.BooleanField(verbose_name="Disponible", default=True)
    tag = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name="Bloque")

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        ordering = ['name']

    def __str__(self):
        #return "[" + str(self.id) + "] " + self.name + " - " + str(os.path.split(self.image.name)[1])
        return self.name

    def __repr__(self):
        return "[" + str(self.id) + "] " + self.name + "\n  - " + str(self.image) + "\n  - Mat/Tec: " + self.details + "\n  - Dimensiones: " + self.size + "\n  - Disponible: " + str(self.disp) + "\n  - Album: " + str(self.tag)
