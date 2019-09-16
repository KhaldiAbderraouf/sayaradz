from rest_framework import generics, status
from rest_framework.generics import ListAPIView, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from option.models import Option
from version.models import Version, Option_Version
from version.serializers import Version_Sereializer, Version_Option_Sereializer, Option_Version_Sereializer


class AllVerions(ListAPIView):
    serializer_class = Version_Option_Sereializer

    def get_queryset(self):
        return Version.objects.all()

class VersionByModele(ListAPIView):
    serializer_class = Version_Option_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs.get('Id_Modele')
        return Version.objects.filter(Id_Modele = Id_Modele)
class VersionByMarque(ListAPIView):
    serializer_class = Version_Option_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs.get('Id_Marque')
        print(Id_Modele)
        return Version.objects.filter(Id_Modele__Id_Marque = Id_Modele)

class NewVersion(generics.ListCreateAPIView):
    queryset = Version.objects.all()
    serializer_class = Version_Option_Sereializer
    # permission_classes = (IsAdminUser,)


class option_version(ListAPIView):
    serializer_class = Option_Version_Sereializer

    def get_queryset(self):
        id_version = self.kwargs['Id_Version']
        return Option_Version.objects.filter(version=id_version).filter(Default = True)

class All_option_version(ListAPIView):
    serializer_class = Option_Version_Sereializer

    def get_queryset(self):
        id_version = self.kwargs['Id_Version']
        return Option_Version.objects.filter(version=id_version)

class add_option(APIView):
    def post(self,request):
        id = request.POST.get('Code_Version')
        version = get_object_or_404(Version, Code_Version=id)
        opts = request.POST.get('Options')
        opts = opts.replace("\"", "")
        opts = opts.replace("]", "")
        opts = opts.replace("[", "")
        opts = opts.split(';')
        default = request.POST.get('Default')
        for i in opts :
            opt = get_object_or_404(Option, Code_Option = i)
            optv = Option_Version.objects.create(option = opt, version = version, Default = default)
            optv.save()
        return Response(status=201)

class Supp(APIView):

    def post(self,request):
        id = request.data['Code_Version']
        version = get_object_or_404(Version,Code_Version = id)
        version.delete()
        return Response(status=201)

class UpdateView(APIView):

    def patch(self, request, pk,new):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Version, Code_Version=pk)
        # this is the only field we want to update
        data = {"Nom_Version": new}
        serializer = Version_Option_Sereializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)