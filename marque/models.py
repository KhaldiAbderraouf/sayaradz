from django.db import models

# Create your models here.

class BaseModel(models.Model):

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'wdland'


class Marque(BaseModel):
    Id_Marque = models.CharField(max_length=10, primary_key=True)
    Nom_Marque = models.CharField(max_length=100)
    Logo = models.ImageField(upload_to='logo', default='logo/default.png', blank=True)
    class Meta:
        abstract = False

