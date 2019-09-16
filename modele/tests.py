from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from marque.models import Marque
from modele.models import Modele


class ModelesAPITestCases(APITestCase):

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        peugeaut = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')

        symbol  = Modele.objects.create(Code_Modele = 'm1', Nom_Modele = 'Symbol', Id_Marque = renault)
        fluance = Modele.objects.create(Code_Modele = 'm2', Nom_Modele = 'fluence', Id_Marque = renault)
        symbol.save()
        fluance.save()

        _206 = Modele.objects.create(Code_Modele='m3', Nom_Modele='206', Id_Marque=peugeaut)
        _207 = Modele.objects.create(Code_Modele='m4', Nom_Modele='207', Id_Marque=peugeaut)
        _206.save()
        _207.save()

    def test_retrieve_all_models(self):

        """
        Vérifie la réussite de GET Request pour récupérer la liste des modèles.
        :return:
        """
        client = APIClient()
        response = client.get('/modele/',format = 'json')
        assert response.status_code == 200

    def test_retrieve_modele_by_marque(self):

        """ Verifie la requette sur un id de marque"""

        client = APIClient()
        response = client.get('/modele/1')
        assert response.status_code == 200

    def test_new(self):
        client = APIClient()
        data = {
            'Code_Modele': "m5",
            'Id_Marque': "1",
            'Nom_Modele': "modele_test",
        }
        try:
            user = Modele.objects.get(Code_Modele = "m5")
        except:
            user = None
        assert user == None
        response = client.post('/modele/new', data)
        assert response.status_code == 201
        expected_user = Modele.objects.get(Code_Modele = "m5")
        assert expected_user != None
        response = client.get('/modele/')
        assert response.status_code == 200
        assert len(response.data) == 5

    def test_delete(self):
        client = APIClient()
        data = {
            'Code_Modele': "m5",
            'Id_Marque': "1",
            'Nom_Modele': "modele_test",
        }
        try:
            user = Modele.objects.get(Code_Modele = "m5")
        except:
            user = None
        assert user == None
        response = client.post('/modele/new', data)
        response = client.get('/modele/')
        assert response.status_code == 200
        assert len(response.data) == 5
        response = client.post('/modele/delete', data)
        assert response.status_code == 201
        response = client.get('/modele/')
        assert len(response.data) == 4

    def test_modif(self):
        client = APIClient()
        response = client.patch('/modele/update/m1/modele_modifier')
        assert response.status_code == 200
        response = client.get('/modele/')
        marque_modifier = response.data[0]
        assert marque_modifier["Nom_Modele"] == "modele_modifier"