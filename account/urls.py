from django.urls import path, include

from . import views
URL_ROOT = '/accounts/'
UTILISATEURS_FABRIQUANT_LIST_END_POINT = 'fabriquant/utlisateur/'
UTILISATEURS_FABRIQUANT_CREATE_END_POINT = 'fabriquan/utlisateur'

urlpatterns = [
    path('', include('rest_framework_social_oauth2.urls')),
    path('fabriquant/utlisateur/<int:Id_Marque>', views.ListUtilisateurFabriquantView.as_view()),
    path('fabriquant/utilisateur',views.FabriquantView.as_view()),
    path('fabriquant',views.AdminFabriquantCreation.as_view()),
    path('fabriquant/utilisateur/<str:email>',views.RUDUtilisateurFabriquant.as_view()),
    path('type',views.UserType.as_view()),
    path('changepassword', views.ChangePasswordView.as_view()),
]