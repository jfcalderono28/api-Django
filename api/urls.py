from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter() #Este router genera automáticamente las URLs necesarias para una API REST.
router.register(r'programmers', views.ProgrammerViewSet ) #programmers' será la URL base de la API (ejemplo: http://localhost:8000/programmers/).
#Django generará automáticamente las rutas para las operaciones CRUD de ProgrammerViewSet.

urlpatterns = [path('', include(router.urls))]
#  '', indica que esta ruta se corresponde con la URL base o principal de la aplicación. Esto significa que la ruta no tendrá un prefijo específico.
# se incluiran todas las rutas generadas por el router

