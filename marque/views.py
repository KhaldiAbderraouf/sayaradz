from rest_framework import generics, status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from marque.models import Marque
from marque.serializers import Marque_Sereializer


class ListeMarques(ListAPIView):
    serializer_class = Marque_Sereializer

    def get_queryset(self):
        return Marque.objects.all()


class NewMarque(generics.ListCreateAPIView):
    queryset = Marque.objects.all()
    serializer_class = Marque_Sereializer
    # permission_classes = (IsAdminUser,)


class Supp(APIView):

    def post(self,request):
        id = request.data['Id_Marque']
        marque = get_object_or_404(Marque,Id_Marque = id)
        marque.delete()
        return Response(status=201)


class UpdateView(APIView):

    def patch(self, request, pk,new):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Marque, Id_Marque=pk)
        # this is the only field we want to update
        data = {"Nom_Marque": new}
        serializer = Marque_Sereializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)