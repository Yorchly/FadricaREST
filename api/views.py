from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.mixins import CheckTokenMixin
from api.models import TipoRoscon, Roscon
from api.serializers import TipoRosconSerializer, RosconSerializer
from api.services.roscon import filter_qs


class ListViewSet(CheckTokenMixin, ListModelMixin, GenericViewSet):
    pass


class ListCreateUpdateViewSet(CheckTokenMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    def put(self, request, *args, **kwargs):
        """
        If put function is not specified, PUT method will not be showed as 'allowed method' in API.
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

    def get_queryset(self):
        """
        Overriding get_queryset in order to process year query param for filtering.
        :return:
        """
        year = self.request.query_params.get("year", None)

        if year:
            qs = filter_qs(anno=year)
        else:
            qs = super(RosconViewSet, self).get_queryset()

        return qs



