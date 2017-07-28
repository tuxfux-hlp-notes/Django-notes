from django.test import TestCase
from .models import Address_Detail

# Create your tests here.



## simple test case to test an url - lets say our home page.

class AddressViewsTestCase(TestCase):
	def test_index(self):						# Any method name starting with test will be run automatically.
		resp = self.client.get('/')
		self.assertEqual(resp.status_code,200)


## this is a test to test your value are workign fine.
## Also we never run our test on a production database as it can screw data.
## so we add some values to the test database and test it .

class AddressTestCase(TestCase):

	# i want to check the values is inserted or not.
	def setUp(self):
		Address_Detail.objects.create(name='chiru',email='chiru1@edu.com',gender='m')

	# i want to test if we are able to retrive the data
	def test_address_student_exist(self):
		student_name = Address_Detail.objects.get(name="chiru",email="chiru1@edu.com")
		self.assertEqual(student_name.email,"chiru1@edu.com")
		self.assertEqual(student_name.name,"chiru")


## fixtures
## mkdir address/fixtures
# python manage.py dumpdata address --indent=4 > address/fixtures/address_views_testdata.json
## so how to use this data for our testing instead of inserting the data.
# work on this tomorrow for student_details

class AddressFixturesTestCase(TestCase):
	fixtures = ['address_views_testdata.json']

	def test_address_fixtures_student_exits(self):
		pass

