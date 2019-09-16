from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Annonce_Image,Annonce,AnnonceOption
from couleur.models import Couleur
from version.models import Version
from account.serializers import  AutomobilisteSerializer
from option.serializers import Option_Sereializer
from option.models import Option
from account.models import Automobiliste
from version.models import Version
from couleur.models import Couleur

class Version_Serializer(serializers.ModelSerializer):
    class Meta:
       model =Version
       fields = [
            'Nom_Version',
            'Code_Version',
            'Id_Modele'

        ]
class Couleur_Serializer(serializers.ModelSerializer):
    class Meta:
       model =Couleur
       fields = [
            'Code_Couleur',
            'Nom_Couleur',

        ]

class Image_Annonce_Sereializer(serializers.ModelSerializer):
    class Meta:
       model =Annonce_Image
       fields = [
            'image'
        ]

class AnnonceOptionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='option.Code_Option')
    name = serializers.ReadOnlyField(source='option.Nom_Option')

    class Meta:
        model = AnnonceOption
        fields = ('id', 'name')
class AutoRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "email")
        super(AutoRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)
class OptionRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "Nom_Option")
        super(OptionRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)
class CouleurRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "Nom_Couleur")
        super(CouleurRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)
class VersionRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "Nom_Version")
        super(VersionRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)
class Annonce_Sereializer(serializers.HyperlinkedModelSerializer):
    automobiliste= AutomobilisteSerializer(read_only=True,many=False)
    Id_Automobiliste = AutoRelatedField(queryset=Automobiliste.objects.all(), many=False)
    Couleur = CouleurRelatedField(queryset=Couleur.objects.all(), many=False)
    Version = VersionRelatedField(queryset=Version.objects.all(), many=False)
    Options = OptionRelatedField(queryset=Option.objects.all(), many=True)
    Images_Annonce = Image_Annonce_Sereializer( many=True,required=False,read_only=False)
    class Meta:
        model = Annonce
        fields = ('Prix_Minimal','Description','automobiliste','Id_Automobiliste','Couleur','Version','Options','Images_Annonce','date')


    @transaction.atomic
    def create(self, validated_data):
        prix=validated_data.pop('Prix_Minimal')
        des=validated_data.pop('Description')
        automobiliste = validated_data.pop('Id_Automobiliste')
        Auto_instance = Automobiliste.objects.get(email=automobiliste.email)
        couleur = validated_data.pop('Couleur')
        couleur_instance= Couleur.objects.get( Code_Couleur=couleur.Code_Couleur)
        version = validated_data.pop('Version')
        version_instance = Version.objects.get(Code_Version = version.Code_Version)
        images_data = self.context.get('view').request.FILES
        options = self.initial_data.get("Options")
        print (options)
        annonce = Annonce.objects.create(Prix_Minimal=prix, Description=des, Id_Automobiliste=Auto_instance,
                                         Couleur=couleur_instance, Version=version_instance)
        for image_data in images_data:
            Annonce_Image.objects.create(Image_Annonce=image_data, Annonce=annonce)
        for option in options:
              Option_instance = Option.objects.get(pk=option)
              AnnonceOption(annonce=annonce, option=Option_instance).save()
              annonce.Options.add(Option_instance)

        annonce.save()
        return annonce


class AnnonceView_Sereializer(serializers.HyperlinkedModelSerializer):
    Images_Annonce = Image_Annonce_Sereializer(many=True, required=False)
    Options = Option_Sereializer(many=True, read_only=True)
    Couleur = Couleur_Serializer(many=False, read_only=True)
    Automobiliste = AutomobilisteSerializer(read_only=True, many=False)
    Version = Version_Serializer(many=False, read_only=True)
    class Meta:
        model = Annonce
        fields = ('Prix_Minimal','Description','Automobiliste', 'Couleur','Version','Options','Images_Annonce','date')



