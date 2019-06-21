from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from marque.models import Marque
from modele.models import Modele
from version.models import Version
from option.models import Option


class OptionsAPITestCases(APITestCase):

    def setUp(self):

        # peugeaut = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        #
        # symbol = Modele.objects.create(Code_Modele='m1', Nom_Modele='Symbol', Id_Marque=peugeaut)
        #
        # version = Version.objects.create(Code_Version='v3', Nom_Version='206', Id_Modele=symbol)
        # version.save()

        option = Option.objects.create(Code_Option='op1', Nom_Option='op1')
        option.save()

    def test_retrieve_all_option(self):

        """
        Vérifie la réussite de GET Request pour récupérer la liste des options.
        :return:
        """
        client = APIClient()
        response = client.get('/option/',format = 'json')
        assert response.status_code == 200

    def test_new(self):
        client = APIClient()
        data = {
            'Code_Option': "op2",
            'Nom_Option': "option_test",
            'Compatible': "v3"
        }
        try:
            user = Option.objects.get(Code_Option = "op2")
        except:
            user = None
        assert user == None
        response = client.post('/option/new', data)
        assert response.status_code == 201
        expected_user = Option.objects.get(Code_Option = "op2")
        assert expected_user != None

    def test_delete(self):
        client = APIClient()
        data = {
            'Code_Option': "op2",
            'Id_Marque': "1",
            'Nom_Option': "option_test",
        }
        try:
            user = Option.objects.get(Code_Option = "op2")
        except:
            user = None
        assert user == None
        response = client.post('/option/new', data)
        response = client.get('/option/')
        assert response.status_code == 200
        assert len(response.data) == 2
        response = client.post('/option/delete', data)
        assert response.status_code == 201
        response = client.get('/option/')
        assert len(response.data) == 1

    def test_modif(self):
        client = APIClient()
        response = client.patch('/option/update/op1/option_modifier')
        print(response)
        assert response.status_code == 200
        response = client.get('/option/')
        marque_modifier = response.data[0]
        assert marque_modifier["Nom_Option"] == "option_modifier"

