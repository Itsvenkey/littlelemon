from django.test import TestCase
from restaurant.models import Menu
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title='IceCream',Price = 80, inventory= 100)
        menu_str = str(item)
        # expected_str = f"{item.Title} - {item.price} - {item.category}"
        self.assertEqual(item,Menu.objects.get(Title = 'IceCream'))
        # self.assertEqual(str(item),"IceCream:80")