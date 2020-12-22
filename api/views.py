from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.models import TipoRoscon, Roscon
from api.serializers import TipoRosconSerializer, RosconSerializer


class ListViewSet(ListModelMixin, GenericViewSet):
    pass


class ListCreateUpdateViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    pass


class TipoRosconListViewSet(ListViewSet):
    queryset = TipoRoscon.objects.all()
    serializer_class = TipoRosconSerializer


class RosconAllView(ListCreateUpdateViewSet):
    queryset = Roscon.objects.all()
    serializer_class = RosconSerializer
