from rest_framework import viewsets
from .serializer import ProgrammerSerializers
from .models import Programmer


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all() #lista de elementos a los cuales se accedera desde el ORM de django 
    serializer_class = ProgrammerSerializers #define qué serializador se utilizará para convertir los datos en JSON y viceversa.

# ORM =object relational mapping 
#El ORM (Object-Relational Mapper) de Django es un sistema que permite interactuar con la base de datos usando código Python en lugar de escribir SQL manualmente.

# Convierte modelos de Python en tablas de base de datos automáticamente.
# Permite realizar consultas sin escribir SQL.
# Funciona con múltiples bases de datos (SQLite, PostgreSQL, MySQL, etc.).