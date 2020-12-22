from rest_framework import serializers
from .models import Roscon, TipoRoscon


class TipoRosconSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRoscon
        fields = ["id", "tipo"]


class RosconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roscon
        fields = ["id", "cantidad", "tipo_roscon", "anno"]
