from rest_framework.generics import UpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.models import TipoRoscon, Roscon
from api.serializers import TipoRosconSerializer, RosconSerializer


class ListViewSet(ListModelMixin, GenericViewSet):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListCreateUpdateViewSet(ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class TipoRosconListViewSet(ListViewSet):
    queryset = TipoRoscon.objects.all()
    serializer_class = TipoRosconSerializer


class RosconViewSet(ListCreateUpdateViewSet):
    queryset = Roscon.objects.all()
    serializer_class = RosconSerializer
