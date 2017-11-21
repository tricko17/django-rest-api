from django.test import TestCase
from rest_framework.test import APIRequestFactory,APITestCase
from ..models import Puppy
from ..serializers import PuppySerializer
from rest_framework import status

class FactoryTest(APITestCase):

    def setUp(self):
        Puppy.objects.create(name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')
        Puppy.objects.create(name='Rambo', age=2, breed='Labrador', color='Black')
        Puppy.objects.create(name='Ricky', age=6, breed='Labrador', color='Brown')
    
    def test_get(self):
        # Create an instance
        response = self.client.get('/api/v1/puppies/')
        print(response.data[0]['name'])
        self.assertEqual(response.status_code, 200)

    def test_get_factory(self):
        # Create an instance
        factory = APIRequestFactory()
        request = factory.get('/api/v1/puppies/')
        response = view(request)
        
        # print(response.data[0]['name'])
        # self.assertEqual(response.status_code, 200)
    

