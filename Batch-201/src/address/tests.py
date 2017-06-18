from django.test import TestCase
from .models import Address_Detail

# Create your tests here.

class AddressTestCase(TestCase):

	# i want to check the values is inserted or not.
	def setUp(self):
		Address_Detail.objects.create(name='chiru',email='chiru1@edu.com',gender='m')

	# i want to test if we are able to retrive the data
	def test_address_student_exist(self):
		student_name = Address_Detail.objects.get(name="chiru",email="chiru1@edu.com")
		self.assertEqual(student_name.email,"chiru1@edu.com")
		self.assertEqual(student_name.name,"chiru")
