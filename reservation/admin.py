from django.contrib import admin

# Register your models here.
from reservation.models import Vehicule, reservations, List_Option

admin.site.register(Vehicule)
admin.site.register(reservations)
admin.site.register(List_Option)