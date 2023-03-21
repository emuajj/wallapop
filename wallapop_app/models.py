from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse

from .models import User

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from PIL import Image






class Usuari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField('Nombre', max_length=120)
    adress=models.CharField(max_length=300)
    zip_code=models.CharField('Codigo Postal', max_length=15)
    phone=models.CharField('Telefono de Conatcto', max_length=25)
    email=models.EmailField('Email de Contacto')
<<<<<<< HEAD
    avatar=models.ImageField(upload_to='images/', blank=True, null=True)
=======
    avatar=models.ImageField(upload_to='profile_images', blank=True, null=True)
>>>>>>> 2049eb3 (Merge branch 'master' of https://github.com/emuajj/wallapop)
    bio = models.TextField(max_length=300)


    def __str__(self):
       return self.name + ' , '+self.email




class Anunci(models.Model):
    foto = models.ImageField('Imagen')
    titol = models.CharField('Asunto', max_length= 300)
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    preu = models.IntegerField('Precio')
    

    def __str__(self):
        return self.titol + ' , ' + str(self.data) + ' , ' + str(self.name)
    
    def get_absolute_url(self):
        return reverse('anunci-details', kwargs={'name':self.id})



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username





    
class Comentari(models.Model):
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    titol = models.ForeignKey(Anunci,on_delete=models.CASCADE,blank=True,null=True)
    data_com = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    id = models.IntegerField('ID', primary_key=True)



    def __str__(self):
        return str(self.titol) + ' , '+ str(self.id)