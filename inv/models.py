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

class Subcategoria(ClaseModelo):
    Categoria=models.Foreignkey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Categoria',

    )

    def __str__(self):
        return '{}:{}'.format(self.categoriadescripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Subcategoria, self).save()
    
    class Meta:
        verbose_name_plural="Sub Categorias"
        unique_together =('categoria','descripcion')

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"


class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_barra')






