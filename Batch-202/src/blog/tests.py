from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone
from tastypie.test import ResourceTestCase

# Create your tests here.

# Example 1: A very simple example on the test cases.
class SimpleTest(TestCase):
	def test_basic_addition(self):
		self.assertEqual(1+1,2)

# Example 2: A example to test if our view is working as expected.
class BlogViewsTestCase(TestCase):
	def test_index(self):
		fixtures = ['blogs_views_testdata.json']
		resp = self.client.get('/blog/pages/')
		self.assertEqual(resp.status_code,200)


## Example 3: A example to test out our rest APIS

class PostResourceTest(ResourceTestCase):
	def test_get_api_json(self):
		resp = self.api_client.get('/blog/api/post/',format='json')
		self.assertValidJSONResponse(resp)







