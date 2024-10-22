from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo): #hereda de moder.url
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Caterogira',
        unique=True
    )

    def _str_(self):
        return '()'.format(self.descripcion)
    
        def save(self):
            self.descripcion = self.descripcion.Upper() #Guarda los datos y los deja en mayuscula en el servidor.
            super(Categoria, self).save()

            class Meta:
                verbose_name_plural= "Categorias"  #Guarda en la clase Categorias.






