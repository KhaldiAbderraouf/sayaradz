from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework import generics
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from couleur.models import Couleur
from couleur.serializers import Couleur_Sereializer


class All_Couleur(ListAPIView):
    serializer_class = Couleur_Sereializer

    def get_queryset(self):
        return Couleur.objects.all()

class Couleur_By_Modele(ListAPIView):
    serializer_class = Couleur_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs['Id_Modele']
        return Couleur.objects.filter(Colore__Code_Modele = Id_Modele)

class Supp(APIView):

    def post(self,request):
        c_id = request.POST.get('Code_Couleur')
        couleur = get_object_or_404(Couleur,Code_Couleur = c_id)
        couleur.delete()
        return Response(status=201)

class New_Couleur(generics.ListCreateAPIView):
    queryset = Couleur.objects.all()
    serializer_class = Couleur_Sereializer