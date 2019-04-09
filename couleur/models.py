from django.db import models

# Create your models here.
from modele.models import Modele


class Couleur(models.Model):
    Code_Couleur = models.CharField(max_length=3, primary_key=True)
    Nom_Couleur = models.CharField(max_length=100)
    Hex_Couleur = models.CharField(max_length=6, default="ffffff")
    Colore = models.ManyToManyField(Modele)

