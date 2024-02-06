from django.test import TestCase
from restaurant import views
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient



class MenuViewTest(TestCase):
    
    def setUp(self):
        Menu.objects.create(Title = 'IceCream', Price = 39 , inventory = 29)
        Menu.objects.create(Title = 'Cream', Price = 9 , inventory = 2)
    
    def test_getall(self):
        queryset = Menu.objects.all()
        
        serializer = MenuSerializer(queryset, many = True)
        
        response = self.client.get('/restaurant/menu/')
        
        self.assertEqual(response.status_code,200)    
        
        self.assertEqual(response.data,serializer.data)
