from django.conf.urls import url
from django.urls import path

from version.views import UpdateView
from . import views

urlpatterns = [
    path('',views.AllVerions.as_view()),
    path('new', views.NewVersion.as_view()),
    path('default', views.add_option.as_view()),
    path('delete', views.Supp.as_view()),
    path('marque/<str:Id_Marque>', views.VersionByMarque.as_view()),
    path('option/<str:Id_Version>', views.All_option_version.as_view()),
    path('default/<str:Id_Version>', views.option_version.as_view()),
    url(r'^update/(?P<pk>[-\w]+)/(?P<new>[-\w]+)$', UpdateView.as_view()),
    path('<str:Id_Modele>', views.VersionByModele.as_view()),

]