import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *

class pfamDescriptionTest(APITestCase):

    pfam1 = None
    pfam2 = None
    good_url = ''
    bad_url = ''

    def setUp(self):
        self.pfam1 =  PfamDescriptionFactory(pfam_id="TestID001")
        self.pfam2 =  PfamDescriptionFactory(pfam_id="TestID001")
        self.good_url = reverse('pfam_get', kwargs={'pk':1})
        self.bad_url = '/api/pfam/123'

    def testMe(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code,200)

    def test_pfamDescriptionReturnFail(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code,200)

class pfamDescriptionSerialiserTest(APITestCase):
    pfam1 = None
    pfamDescriptionSerializer = None

    def setUp(self):
        self.pfam1 = PfamDescriptionFactory(pfam_id="TestID001")
        self.pfamDescriptionSerializer = PfamSerializer(instance=self.pfam1)
    
    def test_pfamDescriptionSerializer(self):
        data = self.pfamDescriptionSerializer.data
        print(data)
        self.assertEqual(set(data.keys()), set(['pfam_id','domain_id']))
        
    def test_pfamDescriptionSerializerHasCorrectData(self):
        data = self.pfamDescriptionSerializer.data
        self.assertEqual(data['pfam_id'],'TestID001')
