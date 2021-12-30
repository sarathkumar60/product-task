from django.test import TestCase
from rest_framework import status
from .models import Product
from rest_framework.test import APITestCase


class ProductTestCase(APITestCase):
    def testcase(self):
        data = {
            "Name": "pepsi",
            "item_cost": 250,
            "stock_quantity": 8

        }
        response = self.client.post("/product/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)