from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.mixins import CheckTokenMixin
from api.models import TipoRoscon, Roscon
from api.serializers import TipoRosconSerializer, RosconSerializer


class ListViewSet(CheckTokenMixin, ListModelMixin, GenericViewSet):
    pass


class ListCreateUpdateViewSet(CheckTokenMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    def put(self, request, *args, **kwargs):
        """
        Si no se especifica la función put, no funciona correctamente el update
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.update(request, *args, **kwargs)


class TipoRosconListViewSet(ListViewSet):
    queryset = TipoRoscon.objects.all()
    serializer_class = TipoRosconSerializer


class RosconViewSet(ListCreateUpdateViewSet):
    queryset = Roscon.objects.all()
    serializer_class = RosconSerializer
