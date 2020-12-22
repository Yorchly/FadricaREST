from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

from api.models import TipoRoscon, Roscon
from api.serializers import TipoRosconSerializer, RosconSerializer


class TipoRosconListView(ListAPIView):
    queryset = TipoRoscon.objects.all()
    serializer_class = TipoRosconSerializer


class RosconAllView(ListAPIView, CreateAPIView, UpdateAPIView):
    queryset = Roscon.objects.all()
    serializer_class = RosconSerializer
