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

