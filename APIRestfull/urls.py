# para USAR url en lugar de PATH
from django.urls import include, path

# es necesario importar las VISTAS de la app
from .views import *

# PARA LAS API
from rest_framework import routers
# libs para logout
from rest_framework.authtoken.views import obtain_auth_token
# Routers para las API (Ej. http://127.0.0.1:8000/panel/api/niveles/)
# La API necesita un Serializador, Vista y esta ruta
router = routers.DefaultRouter()
router.register('Libros', LibrosViewSet)
router.register('Autores', AutoresViewSet)
router.register('Autoria', AutoriaViewSet)
router.register('autoria-personalizada', AutoriaPersonalizadoViewSet, basename='autoria-personalizada')

urlpatterns = [
	path('', include(router.urls), name='api-rest'),
 	path("login_user/", obtain_auth_token, name="login"),
  	path("logout_user/", view=logout_user, name="logout_user"),
    # path('lista_libros/', LibrosList.as_view()),
	# path('detalle_libro/<int:id>/', LibrosDetails.as_view()),
	# path('lista_autores/', AutoresList.as_view()),
	# path('detalle_autores/<int:id>/', AutoresDetails.as_view()),
]