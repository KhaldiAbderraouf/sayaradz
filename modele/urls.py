from django.conf.urls import url
from django.urls import path

from modele.views import UpdateView
from . import views

urlpatterns = [
    path('',views.ListAllModels.as_view()),
    path('<int:Id_Marque>', views.ModelesByMarque.as_view()),
    path('new', views.NewModele.as_view()),
    path('delete', views.Supp.as_view()),
    url(r'^update/(?P<pk>[-\w]+)/(?P<new>[-\w]+)$', UpdateView.as_view()),
]