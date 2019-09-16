from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include

from django.contrib import admin
from django.views.static import serve

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('annonce/', include('annonce.urls')),
    path('account/',include('account.urls')),
    path('marque/',include('marque.urls')),
    path('modele/',include('modele.urls')),
    path('version/',include('version.urls')),
    path('option/', include('option.urls')),
    path('couleur/', include('couleur.urls')),
    path('tarif/', include('tarif.urls')),
    path('reservation/', include('reservation.urls')),
    path('stock/', include('stock.urls')),
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
