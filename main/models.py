from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Producto(models.Model):
	titulo = models.CharField(max_length=140)
	cuerpo = models.TextField()
	precio = models.TextField()
	slug = models.SlugField(max_length=500,blank=True,null=True)
	imagen = models.ImageField(upload_to='files',blank=True,null=True)
	def __str__(self):
		return self.titulo 

# Create your models here.
