from rest_framework import generics, status
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


class UpdateView(APIView):

    def patch(self, request, pk,new):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Modele, Code_Modele=pk)
        # this is the only field we want to update
        data = {"Nom_Modele": new}
        serializer = Modele_Sereializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewModele(generics.ListCreateAPIView):
    queryset = Modele.objects.all()
    serializer_class = Modele_Sereializer
    # permission_classes = (IsAdminUser,)