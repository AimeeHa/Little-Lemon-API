from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Item 1', price=10.99, inventory=100)
        Menu.objects.create(title='Item 2', price=5.99, inventory=50)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu')
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = response.data
        menu_objects = Menu.objects.all()
        self.assertEqual(len(serialized_data), menu_objects.count())

        # Iterate through the serialized data and compare it to the database values
        for i, item_data in enumerate(serialized_data):
            menu_item = menu_objects[i]
            self.assertEqual(item_data['title'], menu_item.title)
            self.assertEqual(float(item_data['price']), float(menu_item.price))
            self.assertEqual(item_data['inventory'], menu_item.inventory)