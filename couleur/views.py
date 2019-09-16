from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from couleur.models import Couleur
from couleur.serializers import Couleur_Sereializer
from modele.models import Modele


class All_Couleur(ListAPIView):
    serializer_class = Couleur_Sereializer

    def get_queryset(self):
        return Couleur.objects.all()

class Couleur_By_Marque(ListAPIView):
    serializer_class = Couleur_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs['Id_Marque']
        modele = Modele.objects.filter(Id_Marque = Id_Modele)
        print(modele)
        res = Couleur.objects.all()
        l = [c for c in res if(len(self.intersection(c.Colore, modele))>0)]

        return l

    def intersection(self,Colore, modele):
        print(Colore)
        print(modele)
        l = [m for m in modele if(m.Code_Modele in Colore)]
        return l


class Couleur_By_Modele(ListAPIView):
    serializer_class = Couleur_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs['Id_Modele']
        return Couleur.objects.filter(Colore__Code_Modele = Id_Modele)

class Supp(APIView):

    def post(self,request):
        c_id = request.data['Code_Couleur']
        couleur = get_object_or_404(Couleur,Code_Couleur = c_id)
        couleur.delete()
        return Response(status=201)

class New_Couleur(generics.ListCreateAPIView):
    queryset = Couleur.objects.all()
    serializer_class = Couleur_Sereializer

class add_modele(APIView):
    def post(self,request):
        id = request.POST.get('Code_Couleur')
        couleur = get_object_or_404(Couleur, Code_Couleur=id)
        opts = request.POST.get('Colore')
        opts = opts.replace("\"", "")
        opts = opts.replace("]", "")
        opts = opts.replace("[", "")
        opts = opts.split(';')
        for i in opts :
            opt = get_object_or_404(Modele, Code_Modele = i)
            couleur.Colore.add(opt)
        couleur.save()
        return Response(status=201)

class UpdateView(APIView):

    def patch(self, request, pk,name,hex):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Couleur, Code_Couleur=pk)
        # this is the only field we want to update
        data = {
            "Nom_Couleur": name,
            "Hex_Couleur": hex,
        }
        serializer = Couleur_Sereializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)