from rest_framework import serializers

from couleur.models import Couleur
from tarif.models import Tarif_Couleur


class Couleur_Sereializer(serializers.ModelSerializer):
    prix = serializers.SerializerMethodField()

    class Meta:
        model = Couleur
        fields = [
            'Code_Couleur',
            'Nom_Couleur',
            'Hex_Couleur',
            'Colore',
            'prix'
        ]

    def get_prix(self, object):
        try:
            prix_v = Tarif_Couleur.objects.filtre(Couleur=object.Code_Couleur)
            f_prix_v = prix_v[0].Prix
            return f_prix_v
        except:
            return 35000