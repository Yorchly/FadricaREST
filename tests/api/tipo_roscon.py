from django.urls import reverse
from rest_framework import status

from api.models import TipoRoscon
from tests.api.common import CommonTests


class TipoRosconTests(CommonTests):
    def setUp(self):
        super(TipoRosconTests, self).setUp()
        self.url = reverse("tiporoscon-list")

    @staticmethod
    def creating_tipo_roscon():
        TipoRoscon.objects.create(tipo="Test")

    def test_get_tipo_roscon(self):
        self.creating_tipo_roscon()

        response = self.client.get("{}?token={}".format(self.url, self.token.token), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.serializer.instance[0].tipo, "Test")

