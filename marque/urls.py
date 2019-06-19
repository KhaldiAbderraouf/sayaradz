from django.conf.urls import url
from django.urls import path

from marque.views import UpdateView
from . import views

urlpatterns = [
    path('', views.ListeMarques.as_view()),
    path('new', views.NewMarque.as_view()),
    path('delete', views.Supp.as_view()),
    url(r'^update/(?P<pk>\d+)/(?P<new>[-\w]+)$', UpdateView.as_view()),
]