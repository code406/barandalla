from django.db import models


class Album(models.Model):
    name = models.CharField(verbose_name="Título", max_length=200)
    cover = models.ImageField(verbose_name="Portada", upload_to='gallery', default='gallery/no-img.jpg')

    class Meta:
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'
    
    def __str__(self):
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

    def __str__(self):
        return self.name
