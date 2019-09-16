from rest_framework import serializers

from tarif.models import Tarif_Version
from version.models import Version, Option_Version


class Version_Sereializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = [
            'Id_Modele',
            'Nom_Version',
            'Code_Version'
        ]
class Option_Version_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Option_Version
        fields = [
            'option',
            'version',
            'Default'
        ]



class Version_Option_Sereializer(serializers.ModelSerializer):
    prix = serializers.SerializerMethodField()

    class Meta:
        model = Version
        fields = [
            'Id_Modele',
            'Nom_Version',
            'Code_Version',
            'option_Version',
            'prix'
        ]
    def get_prix(self,object):
        try:
            prix_v = Tarif_Version.objects.filtre(Version = object.Code_Version)
            f_prix_v = prix_v[0].Prix
            return f_prix_v
        except:
            return 1500000
# class Version_Details_Serializer(serializers.ModelSerializer):
