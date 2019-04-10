from django.db import models

from account.models import Automobiliste
from option.models import Option
from couleur.models import Couleur
from version.models import Version

class Annonce(models.Model):
    Prix_Minimal = models.FloatField()
    Description = models.TextField(blank=True,null=True)
    Id_Automobiliste = models.ForeignKey(Automobiliste,on_delete=models.CASCADE)
    Couleur = models.ForeignKey(Couleur, on_delete=models.CASCADE,null=True,blank=True)
    Version = models.ForeignKey(Version, on_delete=models.CASCADE,blank=True)
    Options= models.ManyToManyField(Option,related_name='Annonces')

class AnnonceOption(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.annonce.Description+ " " + self.option.name

class Annonce_Image(models.Model):
    Images_Annonce = models.ImageField(null=False, upload_to='Annonce/')
    Annonce = models.ForeignKey(Annonce, related_name='Images_Annonce',null=False,default=1,on_delete=models.CASCADE)