from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.files import File 
from django.contrib import admin
from sorl import thumbnail
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail

# Create your models here.

class cliente(models.Model):
    nombre          = models.CharField(max_length=200)
    apellidos       = models.CharField(max_length=200)
    status          = models.BooleanField(default=True)

    def __unicode__(self):
        nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
        return nombreCompleto
    
class producto(models.Model):
    nombre          = models.CharField(max_length=200)     
    descripcion     = models.TextField(max_length=300)
    status          = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre

class artista(models.Model):
	nombre			=models.CharField(max_length=200)
	descripcion		=models.TextField(max_length=300)
	email			=models.CharField(max_length=200)
	web				=models.CharField(max_length=200)
	estilo			=models.CharField(max_length=200)
	image 			=ImageField(upload_to='images/')
	
	
	def __unicode__(self):
		return self.nombre
		
class evento(models.Model):
	nombre			=models.ForeignKey(artista, null= True, blank=True)
	evento			=models.CharField(max_length=200)
	categoria		=models.CharField(max_length=200)
	descripcion		=models.TextField(max_length=300)
	fecha			=models.DateField()
	fechafin		=models.DateField()
	hora			=models.TimeField()

	def __unicode__(self):
		return self.evento
		

class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=50)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.image.name

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "title", "user", "rating", "created"]
    list_filter = ["tags", "albums"]

