from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from reservation.disponibilité.Recherche_Hundler import Recherche_Hundler
from reservation.models import reservations, Vehicule
from reservation.serializers import Commande_Sereializer, Vehicule_Sereializer, Options_Vehicule_Sereializer, \
    Vehicule_Sereializer_Disp, Vehicule_Sereializer_r
import json

class Reservations(ListAPIView):
    serializer_class = Commande_Sereializer

    def get_queryset(self):
        Id_Marque = self.kwargs.get('Id_Marque')
        cmds = reservations.objects.filter(Vendu = False)
        cmds_ids = []
        for o in cmds:
            if (str(o.get_marque()) == str(Id_Marque)):
                cmds_ids.append(o)
        return cmds_ids


class Vehicules(ListAPIView):
    serializer_class = Vehicule_Sereializer

    def get_queryset(self):
        Id_Marque = self.kwargs.get('Id_Marque')
        vehicule = Vehicule.objects.all()
        vehicules = []
        for o in vehicule:
            if (str(o.get_marque()) == str(Id_Marque)):
                vehicules.append(o)
        return vehicules

class Disponible(ListAPIView):
    serializer_class = Vehicule_Sereializer_Disp

    def get_queryset(self):
        v = Vehicule.objects.filter(Vendu = False)
        print(v)
        return v

    def post(self, request):
        critere = request.POST.get('critere')

        rh = Recherche_Hundler()
        l = rh.disponible(critere)

        content = {'reponse': json.dumps(l)}
        return Response(content)

class valider(APIView):

    def post(self, request):
        nm = request.kwargs['Numero_Chassis']
        vehicule = Vehicule.objects.get(Numero_Chassis = nm)
        # draham
        vehicule.Vendu.set(True)
        vehicule.save()

class Commander(generics.ListCreateAPIView):
    queryset = reservations.objects.all()
    serializer_class = Commande_Sereializer


class validated(ListAPIView):
    serializer_class = Commande_Sereializer
    def get_queryset(self):
        Id_user = self.kwargs.get('Automobiliste')
        cmds = reservations.objects.filter(Automobiliste = Id_user)
        return cmds