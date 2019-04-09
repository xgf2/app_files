from django.test import TestCase, Client, SimpleTestCase
import unittest
from django.contrib.auth.models import User

# Create your tests here.

class CheckResponseTemplateForRoot(SimpleTestCase):
	""" Check response template from server for url '/' """	

	def setUp(self):
		self.client = Client()

	def test_details(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'files/index.html')

class CheckAuthenticateUserForDownloadSuccessful(TestCase):
	""" Check authenticate user and response template for successful login  for download
	The user(identifier) and password(code) in the database. """
	
	#@classmethod
	#def setUpTestData(cls):
		#cls.user = User.objects.create(username = 'test', password = 'test')
	
	def setUp(self):
		self.client = Client() #enforce_csrf_checks=True)
		self.user = User.objects.create(username = 'test', password = 'testuser')

	def test_details(self):
		response = self.client.post('/files/authenticateuser', {'username': 'test', 'password': 'testuser', 'download': 'Download'})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'files/list_uploaded_files.html')

class CheckAuthenticateUserForDownloadUnsuccessful(TestCase):
	""" Check authenticate user and response template for UNsuccessful login  for download.
	The user(identifier) and password(code) be absent in the database. """
	
	def setUp(self):
		self.client = Client() 

	def test_details(self):
		response = self.client.post('/files/authenticateuser', {'username': 'test', 'password': 'testuser', 'download': 'Download'})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'files/identifier_not_register.html')
