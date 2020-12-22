from rest_framework import serializers
from .models import Roscon


class RosconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roscon
        fields = ["id", "cantidad", "tipo_roscon", "anno"]
