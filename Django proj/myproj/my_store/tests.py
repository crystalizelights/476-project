from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import time

class TimeTests(TestCase):
     def setUp(self):
        self.username = 'jonesuncle'
        self.password = '@uncle123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
     
     def test_GreetingMessage(self):
        print(f"------------ ------------------ -------------")
        print(f"------------ TESTING PERFOMANCE--------------")
        print(f"------------ ------------------ -------------")
        
     def test_MyStore_LoadingTime(self):
        """Show that the My Store loads in less than a Second"""
        print(f" ")
        print(f"                            TEST                                  ")
        print(f"Testing that the User Settings View returns userSettingsPage.html")
        print(f" ")
        response = self.client.get(reverse('vendor:index'))
        startTime = time.time()
        response = self.client.get(reverse('my_store:index'))
        response = self.client.get(response['Location'])
        endTime = time.time()
        self.assertTrue(endTime - startTime < 1)
        print(f"                            RESULT                                 ")
        print(f"TEST PASSED: My Store page loaded in less than a second")
 
     def test_Login_NavigationTime(self):
        """Show that user after login can be redirected to the page in less than a second"""
        print(f" ")
        print(f"                            TEST                                  ")
        print(f"Testing that  after login user can be redirected to the page in less than a second")
        print(f" ")
        
        startTime = time.time()
        response = self.client.post(reverse('vendor:login'), {
            'username': self.username,
            'password': self.password,
        })
        
        response = self.client.get(response['Location'])
        endTime = time.time()
        self.assertTrue(endTime - startTime < 1)
        print(f"                            RESULT                                 ")
        print(f"TEST PASSED: Redirection took {endTime - startTime} seconds")