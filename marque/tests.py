from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from marque.models import Marque
from marque.serializers import Marque_Sereializer


class Simple_Test(APITestCase):
    def setUp(self):
        renault = Marque.objects.create(Id_Marque = 1, Nom_Marque = 'Renault', Logo = 'default.png')
        renault.save()
        peugeot = Marque.objects.create(Id_Marque = 2, Nom_Marque = 'Peugeot', Logo = 'default.png')
        peugeot.save()

    def test_list(self):
        client = APIClient()
        user = Marque.objects.get(Id_Marque = 1)
        response = client.get('/marque/')
        assert response.status_code == 200
        assert len(response.data) == 2
        # assert serializer.data in response.data

    def test_new(self):
        client = APIClient()
        data = {
            'Id_Marque': "5",
            'Nom_Marque': "marque_test",
        }
        try:
            user = Marque.objects.get(Id_Marque = 5)
        except:
            user = None
        assert user == None
        response = client.post('/marque/new', data)
        assert response.status_code == 201
        expected_user = Marque.objects.get(Id_Marque = 5)
        assert expected_user != None

    def test_delete(self):
        client = APIClient()
        data = {
            'Id_Marque': "5",
            'Nom_Marque': "marque_test",
        }
        try:
            user = Marque.objects.get(Id_Marque = 5)
        except:
            user = None
        assert user == None
        response = client.post('/marque/new', data)
        response = client.get('/marque/')
        assert response.status_code == 200
        assert len(response.data) == 3
        response = client.post('/marque/delete', data)
        assert response.status_code == 201
        response = client.get('/marque/')
        assert len(response.data) == 2

    def test_modif(self):
        client = APIClient()
        response = client.patch('/marque/update/1/marque_modifier')
        print(response.status_code)
        assert response.status_code == 200
        response = client.get('/marque/')
        print(response.data[0])
        marque_modifier = response.data[0]
        assert marque_modifier["Nom_Marque"] == "marque_modifier"