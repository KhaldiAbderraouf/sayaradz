from rest_framework import serializers

from option.models import Option
from tarif.models import Tarif_Option


class Option_Sereializer(serializers.ModelSerializer):
    prix = serializers.SerializerMethodField()

    class Meta:
        model = Option
        fields = [
            'Code_Option',
            'Nom_Option',
            'prix'
        ]

    def get_prix(self, object):
        try:
            prix_v = Tarif_Option.objects.filtre(Option=object.Code_Option)
            f_prix_v = prix_v[0].Prix
            return f_prix_v
        except:
            return 55000
