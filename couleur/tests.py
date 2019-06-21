from django.shortcuts import get_object_or_404
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from couleur.models import Couleur
from marque.models import Marque
from modele.models import Modele
from version.models import Version


class CouleursAPITestCases(APITestCase):

    def setUp(self):

        peugeaut = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        peugeaut.save()

        symbol = Modele.objects.create(Code_Modele='m3', Nom_Modele='Symbol3', Id_Marque=peugeaut)
        symbol.save()
        symbol = Modele.objects.create(Code_Modele='m2', Nom_Modele='Symbol2', Id_Marque=peugeaut)
        symbol.save()
        symbol = Modele.objects.create(Code_Modele='m1', Nom_Modele='Symbol', Id_Marque=peugeaut)
        symbol.save()

        version = Version.objects.create(Code_Version='v3', Nom_Version='206', Id_Modele=symbol)
        version.save()

        couleur = Couleur.objects.create(Code_Couleur='op1', Nom_Couleur='op1')
        l = [symbol]
        couleur.Colore.set(l)
        couleur.save()

    def test_retrieve_all_Couleur(self):

        """
        Vérifie la réussite de GET Request pour récupérer la liste des Couleurs.
        :return:
        """
        client = APIClient()
        response = client.get('/couleur/',format = 'json')
        assert response.status_code == 200

    def test_Couleur_version(self):

        client = APIClient()
        response = client.get('/couleur/m1',format = 'json')
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_new(self):
        client = APIClient()
        data = {
            'Code_Couleur': "c2",
            'Nom_Couleur': "Couleur_test",
            'Hex_Couleur': "000000",
            'Colore':'m1'
        }
        try:
            user = Couleur.objects.get(Code_Couleur = "c2")
        except:
            user = None
        assert user == None
        response = client.post('/couleur/new', data)
        assert response.status_code == 201
        expected_user = Couleur.objects.get(Code_Couleur = "c2")
        assert expected_user != None

    def test_delete(self):
        client = APIClient()
        data = {
            'Code_Couleur': "c2",
            'Nom_Couleur': "Couleur_test",
            'Hex_Couleur': "000000",
            'Colore': 'm1'
        }
        try:
            user = Couleur.objects.get(Code_Couleur = "c2")
        except:
            user = None
        assert user == None
        response = client.post('/couleur/new', data)
        response = client.get('/couleur/')
        assert response.status_code == 200
        assert len(response.data) == 2
        response = client.post('/couleur/delete', data)
        assert response.status_code == 201
        response = client.get('/couleur/')
        assert len(response.data) == 1

    def test_modif(self):
        client = APIClient()
        response = client.patch('/couleur/update/op1/Couleur_modifier/ff00ff')
        assert response.status_code == 200
        response = client.get('/couleur/')
        marque_modifier = response.data[0]
        assert marque_modifier["Nom_Couleur"] == "Couleur_modifier"

    def test_add_modele(self):
        client = APIClient()
        data = {
            'Code_Couleur': 'op1',
            'Colore': ["m3","m2"]
        }
        response = client.post('/couleur/modele',data)
        assert response.status_code == 201


