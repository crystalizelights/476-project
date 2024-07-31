from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Test for the login Page
class LoginPageTests(TestCase):
    # Acount Details
    def setUp(self):
        self.username = 'jonesuncle'
        self.password = '@uncle123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    def test_GreetingMessgae(self):
        print(f"------------ ------------------ -------------")
        print(f"------------ TESTING LOGIN PAGE--------------")
        print(f"-------- Test username: {self.username} ---------")
        print(f"-------- Test password: {self.password} --------")
        print(f"------------ ------------------ -------------")
    
    def test_LoginSuccess(self):
        """Show that user can correctly login"""
        print(f" ")
        print(f"Testing that user can correctly login with correct credentials")
        print(f"Test username: {self.username} Test password: {self.password} ")
        print(f" ")
        
        response = self.client.post(reverse('vendor:login'), {
            'username': self.username,
            'password': self.password,
        })
        
        print(f"Status code: {response.status_code}")
        
        # if login was succesful there should be a redirect
        self.assertEqual(response.status_code, 302)
        print("Test Passed:Login successful, Status code is 302")
        

    def test_LoginFail(self):
        """Show that If users inputs wrong credential it will throw an error"""
        print(f" ")
        print(f"Testing that If users inputs wrong credentials it will throw an error")
        print(f"Test username: {self.username} Test password: badPassword ")
        print(f" ")
        
        response = self.client.post(reverse('vendor:login'), {
          'username': self.username,
          'password': 'bad Password',
        })
        
        # login form should show this message if the login info dont match
        self.assertContains(response, "Please enter a correct username and password.")
        print("Test Passed: Login Failed, Error message found.")
        
        
 