from django.conf.urls import url
from django.urls import path

from couleur.views import UpdateView
from . import views

urlpatterns = [
    path('', views.All_Couleur.as_view()),
    path('modele', views.add_modele.as_view()),
    path('new', views.New_Couleur.as_view()),
    path('delete', views.Supp.as_view()),
    path('<str:Id_Modele>', views.Couleur_By_Modele.as_view()),
    url(r'^update/(?P<pk>[-\w]+)/(?P<name>[-\w]+)/(?P<hex>[-\w]+)$', UpdateView.as_view()),
]