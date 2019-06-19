from rest_framework import generics
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from modele.models import Modele
from modele.serializers import Modele_Sereializer


class ModelesByMarque(ListAPIView):
    """Retourne tous les modèles du systeme relativement à une marque"""

    serializer_class = Modele_Sereializer

    def get_queryset(self):
        id_marque = self.kwargs['Id_Marque']
        return Modele.objects.filter(Id_Marque = id_marque)


class ListAllModels(ListAPIView):
    """Retourne tout les modèles du système"""
    serializer_class = Modele_Sereializer

    def get_queryset(self):
        return Modele.objects.all()

class Supp(APIView):

    def post(self,request):
        id = request.POST.get('Code_Modele')
        modele = get_object_or_404(Modele,Code_Modele = id)
        modele.delete()
        return Response(status=201)


class NewModele(generics.ListCreateAPIView):
    queryset = Modele.objects.all()
    serializer_class = Modele_Sereializer
    # permission_classes = (IsAdminUser,)