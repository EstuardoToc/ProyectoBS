from django.db import models
from django.contrib.auth.models import User

class ClaseModelo(models.Model):

    estado = models.BooleanField(default=True) #modelo de la base

    fc = models.DateField(auto_now_add=True) #fecha de creacion cuando el registro se cree
   
    fn = models.DateTimeField(auto_now=True)  #fecha de modificado

    uc = models.ForeignKey(User, on_delete=models.CASCADE) #un usuario en mucho

    um = models.IntegerField(blank=True, null=True)
    
    
    class Meta: #modelo de tipo abstracto para notificar a django que no tome el modelo en cuenta
        abstract = True