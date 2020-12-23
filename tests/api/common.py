from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Token


class CommonTests(APITestCase):
    def setUp(self):
        self.token = Token.objects.create()
        self.url = ""

    def test_get_method_no_token(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_method_no_token(self):
        response = self.client.post(self.url, data={"test": "test"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_method_no_token(self):
        response = self.client.post(self.url, data={"test": "test"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_method_no_token(self):
        response = self.client.delete(self.url, data={"test": "test"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        self.token.delete()
