from django.urls import reverse
from rest_framework import status

from api.models import TipoRoscon, Roscon
from tests.api.common import CommonTests


class RosconesTests(CommonTests):
    def setUp(self):
        super(RosconesTests, self).setUp()
        self.url = reverse("roscon-list")
        self.url_with_token = "{}?token={}".format(self.url, self.token.token)

        self.populating_db()

    def populating_db(self):
        tipo_roscon = TipoRoscon.objects.create(tipo="TestInRoscones")
        tipo_roscon_2 = TipoRoscon.objects.create(tipo="TestInRoscones2")
        self.roscon_1 = Roscon.objects.create(cantidad=500, tipo_roscon=tipo_roscon, anno=2020)
        self.roscon_2 = Roscon.objects.create(cantidad=200, tipo_roscon=tipo_roscon_2, anno=2021)

    def test_get_method(self):
        response = self.client.get(self.url_with_token, format='json')
        qs = response.data.serializer.instance

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(qs[0], self.roscon_1)
        self.assertEqual(qs[1], self.roscon_2)

    def test_get_with_year(self):
        response = self.client.get("{}&year={}".format(self.url_with_token, 2020), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get("anno"), 2020)

    def test_post_method(self):
        response = self.client.post(
            self.url_with_token,
            {'cantidad': 300, "tipo_roscon": self.roscon_1.tipo_roscon.pk, "anno": 2030},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.serializer.instance, Roscon.objects.last())

    def test_put_method(self):
        response = self.client.put(
            "{}{}/?token={}".format(self.url, self.roscon_1.pk, self.token.token),
            {'cantidad': 50, "tipo_roscon": self.roscon_1.tipo_roscon.pk, "anno": 2022},
            format='json'
        )
        # It is needed to get roscon_1 value again to see the changes.
        roscon = Roscon.objects.get(id=self.roscon_1.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(roscon.cantidad, 50)
        self.assertEqual(roscon.anno, 2022)
