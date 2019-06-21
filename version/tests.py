from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json

from marque.models import Marque
from modele.models import Modele
from option.models import Option
from version.models import Version


class VersionApiTest(APITestCase):
    def setUp(self):
        marque = Marque.objects.create(Id_Marque=1, Nom_Marque='BMW')
        marque.save()
        modele = Modele.objects.create(Code_Modele=1, Nom_Modele='MODELE',Id_Marque=marque)
        modele.save()
        option1 = Option.objects.create(Code_Option='op1', Nom_Option='op1')
        option1.save()
        option2 = Option.objects.create(Code_Option='op2', Nom_Option='op2')
        option2.save()
        version=Version.objects.create(Code_Version=1,Nom_Version='Version1',Id_Modele=modele)
        version.save()
        version=Version.objects.create(Code_Version=2,Nom_Version='Version2',Id_Modele=modele)
        version.save()

    def test_retrieve_all_versions(self):
        """Test si le client est capable de retrouver toutes les marques avec un get request"""
        client = APIClient()
        response = client.get('/version/', format = 'json')
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_all_by_modele(self):
        client = APIClient()
        response = client.get('/version/1')
        assert response.status_code == 200
        assert len(response.data) == 2


    def test_new(self):
        client = APIClient()
        data = {
            'Code_Version': 3,
            'Nom_Version': "version_test",
            'Id_Modele': 1
        }
        try:
            user = Version.objects.get(Code_Version = 3)
        except:
            user = None
        assert user == None
        response = client.post('/version/new', data)
        assert response.status_code == 201
        expected_user = Version.objects.get(Code_Version = 3)
        assert expected_user != None

    def test_delete(self):
        client = APIClient()
        data = {
            'Code_Version': 3,
            'Nom_Version': "version_test",
            'Id_Modele': 1
        }
        try:
            user = Version.objects.get(Code_Version = 3)
        except:
            user = None
        assert user == None
        response = client.post('/version/new', data)
        response = client.get('/version/')
        assert response.status_code == 200
        assert len(response.data) == 3
        response = client.post('/version/delete', data)
        assert response.status_code == 201
        response = client.get('/version/')
        assert len(response.data) == 2

    def test_modif(self):
        client = APIClient()
        response = client.patch('/version/update/1/version_modifier')
        assert response.status_code == 200
        response = client.get('/version/')
        marque_modifier = response.data[0]
        assert marque_modifier["Nom_Version"] == "version_modifier"

    def test_add_option(self):
        client = APIClient()
        data = {
            'Code_Version': 1,
            'Default': True,
            'Options':["op1","op2"]
        }
        response = client.post('/version/default', data)
        assert response.status_code == 201

    def test_option_version(self):
        client = APIClient()
        data = {
            'Code_Version': 1,
            'Default': True,
            'Options': ["op1"]
        }
        response = client.post('/version/default', data)
        data = {
            'Code_Version': 1,
            'Default': False,
            'Options': ["op2"]
        }
        response = client.post('/version/default', data)
        assert response.status_code == 201
        response = client.get('/version/default/1')
        assert response.status_code == 200
        assert len(response.data) == 1
        response = client.get('/version/option/1')
        assert response.status_code == 200
        assert len(response.data) == 2

