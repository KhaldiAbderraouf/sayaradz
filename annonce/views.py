
# Create your views here.
from django import forms
from django.contrib.admin import ModelAdmin
from requests import Response
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from rest_framework.templatetags.rest_framework import data
from rest_framework.viewsets import ModelViewSet
from .serializers import Annonce_Sereializer,AnnonceView_Sereializer
from .models import *

class Annonce_Liste(generics.ListCreateAPIView):
    serializer_class = Annonce_Sereializer
    queryset = Annonce.objects.all()


class Annonce_By_Automobiliste(ListAPIView):
    """Retourne toutes les annonces d'un automobiliste"""

    serializer_class = AnnonceView_Sereializer

    def get_queryset(self):
        id_automobiliste = self.kwargs['Id_Automobiliste']
        return Annonce.objects.filter(Id_Automobiliste = id_automobiliste)



class List_All_Annonce(ListAPIView):
    serializer_class = AnnonceView_Sereializer
    def get_queryset(self):
      return Annonce.objects.all()





