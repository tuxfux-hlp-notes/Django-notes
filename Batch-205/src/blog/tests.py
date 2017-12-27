from django.test import TestCase

# Create your tests here.


# a basic test ##
class SimpleTest(TestCase):
	def test_basic_addition(self):
		self.assertEqual(1+1,2)

## a blog view test case 
class BlogViewsTestCase(TestCase):
	def test_index(self):
		resp = self.client.get('/blog/')
		self.assertEqual(resp.status_code,200)

## a rest api test case.
## A tastepie.test issue for import in latest version 
## works better for django-tastypie==0.13.3

from tastypie.test import ResourceTestCase

class PostResourceTest(ResourceTestCase):
	def test_get_api_json(self):
		resp = self.api_client.get('/api/post/',format='json')
		self.assertValidJSONResponse(resp)