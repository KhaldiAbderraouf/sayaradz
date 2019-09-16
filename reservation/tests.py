from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from account.models import Fabriquant, Automobiliste
from couleur.models import Couleur
from marque.models import Marque
from modele.models import Modele
from option.models import Option
from reservation.models import Vehicule, reservations
from version.models import Version


class CouleursAPITestCases(APITestCase):

    def setUp(self):

        peugeaut = Marque.objects.create(Id_Marque=1, Nom_Marque='Peugeot')
        peugeaut.save()
        chevroley = Marque.objects.create(Id_Marque=2, Nom_Marque='chevroley')
        chevroley.save()

        user1 = Automobiliste.objects.create_user("admin@peugeot.dz")
        user1.save()
        user2 = Automobiliste.objects.create_user("user1@peugeot.dz")
        user2.save()
        user3 = Automobiliste.objects.create_user("user2@peugeot.dz")
        user3.save()

        m1 = Modele.objects.create(Code_Modele='m1', Nom_Modele='m1', Id_Marque=peugeaut)
        m1.save()
        m2 = Modele.objects.create(Code_Modele='m2', Nom_Modele='m2', Id_Marque=peugeaut)
        m2.save()
        m3 = Modele.objects.create(Code_Modele='m3', Nom_Modele='m3', Id_Marque=chevroley)
        m3.save()
        m4 = Modele.objects.create(Code_Modele='m4', Nom_Modele='m4', Id_Marque=chevroley)
        m4.save()

        version1 = Version.objects.create(Code_Version='v1', Nom_Version='201', Id_Modele=m1)
        version1.save()
        version2 = Version.objects.create(Code_Version='v2', Nom_Version='202', Id_Modele=m2)
        version2.save()
        version3 = Version.objects.create(Code_Version='v3', Nom_Version='203', Id_Modele=m2)
        version3.save()
        version4 = Version.objects.create(Code_Version='v4', Nom_Version='204', Id_Modele=m3)
        version4.save()
        version5 = Version.objects.create(Code_Version='v5', Nom_Version='205', Id_Modele=m4)
        version5.save()
        version6 = Version.objects.create(Code_Version='v6', Nom_Version='206', Id_Modele=m4)
        version6.save()

        couleur = Couleur.objects.create(Code_Couleur='c1', Nom_Couleur='c1')
        l = [m1,m2,m3,m4]
        couleur.Colore.set(l)
        couleur.save()

        option1 = Option.objects.create(Code_Option='op1', Nom_Option='op1')
        option1.save()
        option2 = Option.objects.create(Code_Option='op2', Nom_Option='op2')
        option2.save()

        vehicule1 = Vehicule.objects.create(Numero_Chassis = '111', Code_Version = version1,Code_Couleur = couleur)
        o = [option1,option2]
        vehicule1.Liste_Option.set(o)
        vehicule1.save()

        vehicule2 = Vehicule.objects.create(Numero_Chassis='222', Code_Version=version2, Code_Couleur=couleur)
        o = [option1]
        vehicule2.Liste_Option.set(o)
        vehicule2.save()

        vehicule3 = Vehicule.objects.create(Numero_Chassis='333', Code_Version=version3, Code_Couleur=couleur)
        o = [option1, option2]
        vehicule3.Liste_Option.set(o)
        vehicule3.save()

        vehicule4 = Vehicule.objects.create(Numero_Chassis='444', Code_Version=version4, Code_Couleur=couleur)
        o = [option2]
        vehicule4.Liste_Option.set(o)
        vehicule4.save()

        vehicule5 = Vehicule.objects.create(Numero_Chassis='555', Code_Version=version5, Code_Couleur=couleur)
        o = [option1, option2]
        vehicule5.Liste_Option.set(o)
        vehicule5.save()

        vehicule6 = Vehicule.objects.create(Numero_Chassis='666', Code_Version=version6, Code_Couleur=couleur)
        o = [option1]
        vehicule6.Liste_Option.set(o)
        vehicule6.save()

        reservation1 = reservations.objects.create(automobiliste = user1, vehicule = vehicule1)
        reservation1.save()
        reservation2 = reservations.objects.create(automobiliste = user1, vehicule = vehicule4)
        reservation2.save()
        reservation3 = reservations.objects.create(automobiliste = user2, vehicule = vehicule6)
        reservation3.save()

    def test_commander(self):
        client = APIClient()
        data = {
            'automobiliste':"user1@peugeot.dz",
            'vehicule':"222"
        }
        response = client.post('/reservation/commande/new', data)
        assert response.status_code == 201

        data = {
            'automobiliste': "user1@peugeot.dz",
            'vehicule': "252"
        }
        response = client.post('/reservation/commande/new', data)
        assert response.status_code == 400

        data = {
            'automobiliste': "r1@peugeot.dz",
            'vehicule': "222"
        }
        response = client.post('/reservation/commande/new', data)
        assert response.status_code == 400

    def test_valider(self):
        client = APIClient()
        data = {
            'Num_Cmd': "2"
        }
        response = client.post('/reservation/valider', data)
        assert response.status_code == 200

        data = {
            'Num_Cmd': "252"
        }
        response = client.post('/reservation/valider', data)
        assert response.status_code == 404

    def test_reservations(self):
        client = APIClient()
        response = client.get('/reservation/commande/1')
        assert response.status_code == 200
        assert len(response.data) == 1

        response = client.get('/reservation/commande/2')
        assert response.status_code == 200
        assert len(response.data) == 2

        response = client.get('/reservation/commande/3')
        assert response.status_code == 200
        assert len(response.data) == 0

    def test_reservations_valider(self):
        client = APIClient()
        response = client.get('/reservation/commande/2')
        assert response.status_code == 200
        assert len(response.data) == 2
        # print(response.data)
        data = {
            'Num_Cmd': "3"
        }
        response = client.post('/reservation/valider', data)
        assert response.status_code == 200
        response = client.get('/reservation/commande/valider/2')
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_list_reservation_auto(self):
        client = APIClient()
        response = client.get('/reservation/Automobiliste/admin@peugeot.dz')
        assert response.status_code == 200
        assert len(response.data) == 2
        response = client.get('/reservation/Automobiliste/user2@peugeot.dz')
        assert response.status_code == 200
        assert len(response.data) == 0



