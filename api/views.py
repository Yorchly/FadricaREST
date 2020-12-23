from django.http import HttpResponseForbidden
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.models import TipoRoscon, Roscon
from api.serializers import TipoRosconSerializer, RosconSerializer
from api.utils import check_token


class ListViewSet(ListModelMixin, GenericViewSet):
    def dispatch(self, request, *args, **kwargs):
        if check_token(self.request.GET.get("token", None)):
            return super(ListViewSet, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()


class ListCreateUpdateViewSet(ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    def dispatch(self, request, *args, **kwargs):
        if check_token(self.request.GET.get("token", None)):
            return super(ListCreateUpdateViewSet, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

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
