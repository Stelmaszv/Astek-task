from rest_framework import status
from django.urls import resolve
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import Client
from .views import CartList
from .models import Cart

class AbstratTest(APITestCase):
    many=True
    url_test=''

    def data_match(self):
        response = self.client.get(self.url_test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def view_match(self,view):
        self.assertEquals(resolve(self.url_test).func.view_class, view)

class CarList_test(AbstratTest):
    url_test = reverse("cars_list", kwargs={})
    url_test_delete = reverse("car_delete", kwargs={"id":0})

    def setUp(self):
        self.client = Client()

    def test_data_match_and_view_match(self):
        self.data_match()
        self.view_match(CartList)
    def test_add_car(self):
        data_post= {
            "make": "Cart",
            "description": "qgqg qgqrg qg qrgqrgqgqrg"
        }
        self.assertEqual(Cart.objects.count(), 0)
        response = self.client.post(self.url_test, data_post)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)