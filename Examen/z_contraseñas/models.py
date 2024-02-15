from django.db import models

'''
class Gestor(models.Model):
    usuario = models.CharField(max_length=12)
    contra = models.CharField(max_length=24)
'''
#----------------EXAMEN--------------
class Gestor(models.Model):
    dni = models.CharField(max_length=12)
    contra = models.CharField(max_length=24)
