from enum import unique
from tkinter.messagebox import YES
from unicodedata import decimal
from django.db import models

class Repositorio (models.Model):
    codigo = models.DecimalField(max_digits=5, decimal_places=0, primary_key=True)
    descricao = models.CharField(max_length=800)
    materia = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='uploads/', blank=True)