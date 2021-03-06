from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from annonce.models import Annonce
from account.models import Automobiliste
from couleur.models import Couleur
from version.models import Version
from marque.models import Marque
from modele.models import Modele

class AnnoncesAPITestCases(APITestCase):

    def setUp(self):
        peugeaut = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        _206 = Modele.objects.create(Code_Modele='m3', Nom_Modele='206', Id_Marque=peugeaut)
        _206.save()
        Version1 = Version.objects.create(Code_Version='v1',Nom_Version='version1', Id_Modele=_206)
        Version1.save()
        Couleur1= Couleur.objects.create(Code_Couleur='1',Nom_Couleur='Noir')
        Couleur1.save()
        Auto1 =Automobiliste.objects.create()
        Auto1.save()
        annonce= Annonce.objects.create(Prix_Minimal=120089833.0,Description='A vendre',Id_Automobiliste=Auto1,Couleur=Couleur1,Version=Version1)
        annonce.save()

    def test_retrieve_all_Annonce(self):
        """
        Vérifie la réussite de GET Request pour récupérer la liste des Annonces.
        """
        client = APIClient()
        response = client.get('/annonce/',format = 'json')
        assert response.status_code == 200
    def test_retrieve_Annonce_by_Automobiliste(self):

        """ Verifie la requette sur un id d'un automobiliste"""

        client = APIClient()
        response = client.get('/annonce/1')
        assert response.status_code == 200

#
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from couleur.models import Couleur
# from marque.models import Marque
# from modele.models import Modele
# from option.models import Option
#
# from version.models import Version
# from option.models import Option
#
# from account.models import Automobiliste
# from annonce.serializers import Annonce_Sereializer
#
# from annonce.models import Annonce
#
# from annonce.models import Annonce_Option, Annonce_Image
#
#
# class TestAnnounceMethods(APITestCase):
#
#     def setUp(self):
#         self.serializer = Annonce_Sereializer()
#
#         self.description = "nouvelle"
#
#         self.prix_Annonce= 1200000.0
#
#         renault = self.insert_marque('R1','Renault')
#         symbole = self.insert_model('M1',renault,'Symbole')
#
#         self.couleur=self.insert_color(21561 )
#
#         self.version = self.insert_version(32165,symbole)
#
#         self.option1=self.insert_option(321842)
#         self.option2=self.insert_option(654321)
#         self.option3=self.insert_option(654218)
#
#         self.automobiliste = Automobiliste.objects.create_user("auto1@gmail.dz", password="testauto1")
#         self.automobiliste.save()
#
#         annonce = Annonce.objects.create(rix_Minimal=self.prix_Annonce, Description=self.description,
#                                          Id_Automobiliste=self.automobiliste,
#                                          Couleur=self.couleur, Version=self.version)
#
#         option_annonce1 = Annonce_Option.objects.create(annonce=annonce, option=self.option1)
#         option_annonce1.save()
#         annonce.Options_Annonce.add(option_annonce1)
#         option_annonce2 = Annonce_Option.objects.create(annonce=annonce, option=self.option2)
#         option_annonce2.save()
#         annonce.Options_Annonce.add(option_annonce2)
#         option_annonce3 = Annonce_Option.objects.create(annonce=annonce, option=self.option3)
#         option_annonce3.save()
#         annonce.Options_Annonce.add(option_annonce3)
#         images=Annonce_Image.object.create(Images_Annonce=self.temporary_image(),Annonce=annonce)
#         images.save()
#         annonce.save()
#     pass
#
#     def insert_color(self, Code_Couleur):
#         couleur = Couleur(Code_Couleur=Code_Couleur)
#         couleur.save()
#
#         pass
#
#     def insert_version(self, Code_Version, Modele):
#         version = Version(Code_Version = Code_Version, Id_Modele= Modele)
#         version.save()
#         pass
#
#     def insert_option(self, Code_option):
#         option = Option(Code_Option= Code_option)
#         option.save()
#         pass
#
#     def insert_model(self, Id_Modele,marque,nom):
#         modele = Modele.objects.create(Code_Modele= Id_Modele, Id_Marque= marque, Nom_Modele= nom)
#         return modele
#
#     def insert_marque(self, Id_Marque, Nom_Marque):
#         marque = Marque.objects.create(Id_Marque = Id_Marque, Nom_Marque =  Nom_Marque)
#         marque.save()
#         return marque
#
#     def temporary_image(self):
#         """
#         Returns a new temporary image file
#         """
#         import tempfile
#         from PIL import Image
#
#         image = Image.new('RGB', (100, 100))
#         tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
#         image.save(tmp_file, 'jpeg')
#         tmp_file.seek(0)  # important because after save(), the fp is already at the end of the file
#         return tmp_file
#     def test_Post_Request(self):
#         data = {
#             'Prix_Minimal': self.prix_Annonce,
#             'Description': self.description,
#             'Id_Automobiliste': self.automobiliste.email,
#             'Couleur': self.couleur.Code_Couleur,
#             'Version': self.version.Code_Version,
#             'Options_Annonce':self.option1.Code_Option,
#             'Images_Annonce':self.temporary_image(),
#         }
#         response = self.client.post("/annonces/CreerAnnonce/", data, format='multipart')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     def test_Annonce(self):
#         client = APIClient()
#         response = client.get('/annonces/', format='json')
#         assert response.status_code == 200