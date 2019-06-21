from django.conf.urls import url
from django.urls import path

from option.views import UpdateView
from . import views

urlpatterns = [
    path('',views.List_All_Options.as_view()),
    path('new', views.New_Option.as_view()),
    path('version/<str:Id_Version>', views.Option_Version.as_view()),
    path('delete', views.Supp.as_view()),
    url(r'^update/(?P<pk>[-\w]+)/(?P<new>[-\w]+)$', UpdateView.as_view()),
]