from couleur.models import Couleur
from option.models import Option
from tarif.models import Tarif_Version, Tarif_Option, Tarif_Couleur
from dateutil.parser import parse

from tarif.serializers import Tarif_Option_Sereializer, Tarif_Version_Sereializer, Tarif_Couleur_Sereializer
from version.models import Version


class Tarif_Builder():
    def Tarif_Handle(self,file):
        for raw in file:
            row = raw.decode("utf-8")
            try:
                r = row.split(";")
                self.create_tarif(r)
            except:
                return False
        return True

    def create_tarif(self,r):
        if(r[0].strip()=="0"):
            self.save_version(r)
        elif(r[0].strip()=="2"):
            self.save_option(r)
        else:
            self.save_couleur(r)

    def save_version(self,r):
        cdv = Version.objects.get(Code_Version = r[1])
        if cdv :
            dtd = parse(r[2])
            dtf = parse(r[3])
            px = float(r[4])
            tarif_Version = Tarif_Version.objects.create(Version = cdv, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
            serializer = Tarif_Version_Sereializer(tarif_Version)
            if serializer.is_valid():
                    serializer.save()

    def save_option(self,r):
        cdo =  Option.objects.get(Code_Option = r[1])
        if cdo :
            dtd = parse(r[2])
            dtf = parse(r[3])
            px = float(r[4])
            tarif_Option = Tarif_Option.objects.create(Option = cdo, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
            serializer = Tarif_Option_Sereializer(tarif_Option)
            if serializer.is_valid():
                serializer.save()

    def save_couleur(self,r):
        cdc = Couleur.objects.get(Code_Couleur = r[1])
        if cdc :
            dtd = parse(r[2])
            dtf = parse(r[3])
            px = float(r[4])
            tarif_Couleur = Tarif_Couleur.objects.create(Couleur = cdc, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
            serializer = Tarif_Couleur_Sereializer(tarif_Couleur)
            if serializer.is_valid():
                serializer.save()