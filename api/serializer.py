from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Programmer
        fields = '__all__' #Indica que se deben serializar todos los campos del modelo.
        

        




