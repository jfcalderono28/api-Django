from django.contrib import admin
from .models import Programmer

admin.site.register(Programmer)
#Cuando se agrega esta línea en el archivo admin.py dentro de una aplicación de Django, le indica al sistema de administración de Django que el modelo Programmer debe aparecer en la interfaz de administración.

# Register your models here.
