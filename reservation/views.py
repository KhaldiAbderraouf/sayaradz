from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView

from reservation.disponibilité.Recherche_Hundler import Recherche_Hundler
from reservation.models import reservations, Vehicule
from reservation.serializers import Commande_Sereializer, Vehicule_Sereializer, Options_Vehicule_Sereializer, \
    Vehicule_Sereializer_Disp, Vehicule_Sereializer_r, vehicule_save
import json

class Reservations(ListAPIView):
    serializer_class = Commande_Sereializer

    def get_queryset(self):
        Id_Marque = self.kwargs.get('Id_Marque')
        cmds = reservations.objects.filter(vehicule__Vendu = False)
        cmds_ids = []
        for o in cmds:
            if (str(o.get_marque()) == str(Id_Marque)):
                cmds_ids.append(o)
        return cmds_ids

class Reservations_valider(ListAPIView):
    serializer_class = Commande_Sereializer

    def get_queryset(self):
        Id_Marque = self.kwargs.get('Id_Marque')
        cmds = reservations.objects.filter(vehicule__Vendu = True)
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
        l = [i for i in v if (not i.Reservation)]
        return l

    def post(self, request):
        critere = request.POST.get('critere')

        rh = Recherche_Hundler()
        l = rh.disponible(critere)

        content = {'reponse': json.dumps(l)}
        return Response(content)

class valider(APIView):

    def post(self, request):
        nc = request.data['Num_Cmd']
        # print(nc)
        try:
            reservation = get_object_or_404(reservations, pk = nc)
            # print(reservation)
            # draham
            data = {
                'accepter': True
            }
            serializer = Commande_Sereializer(reservation, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()

            # nm = reservation.vehicule
            # print(nm)
            vehicule = reservation.vehicule
            # print(vehicule)
            data = {
                'Vendu':True
            }
            serializer = vehicule_save(vehicule, data=data, partial=True)
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=404)

class Commander(generics.ListCreateAPIView):
    queryset = reservations.objects.all()
    serializer_class = Commande_Sereializer


class validated(ListAPIView):
    serializer_class = Commande_Sereializer
    def get_queryset(self):
        Id_user = self.kwargs.get('Automobiliste')
        cmds = reservations.objects.filter(automobiliste = Id_user)
        return cmds