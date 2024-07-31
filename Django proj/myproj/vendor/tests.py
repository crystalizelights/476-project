from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Test for the login Page //
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
        print(f"                            TEST                                  ")
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
        print(f"                            RESULT                                 ")
        print("TEST PASSED:Login successful, Status code is 302")
        
    def test_LoginFail(self):
        """Show that If users inputs wrong credential it will throw an error"""
        print(f" ")
        print(f"                            TEST                                  ")
        print(f"Testing that If users inputs wrong credentials it will throw an error")
        print(f"Test username: {self.username} Test password: badPassword ")
        print(f" ")
        
        response = self.client.post(reverse('vendor:login'), {
          'username': self.username,
          'password': 'bad Password',
        })
        
        # login form should show this message if the login info dont match
        self.assertContains(response, "Please enter a correct username and password.")
        print(f"                            RESULT                                 ")
        print("TEST PASSED: Login Failed, Error message found.")
           
    def test_Login_EmptyForm(self):
        """Show that If the fields are empty it will throw an error"""
        print(f" ")
        print(f"                            TEST                                  ")
        print(f"Testing that If the fields are empty emails it will throw an error")
        print(f"Test username: Test password: ")
        print(f" ")
        
        response = self.client.post(reverse('vendor:login'), {
            
        })
        
        # login form should show this message if the fields are empty
        self.assertContains(response, "This field is required")
        print(f"                            RESULT                                 ")
        print("TEST PASSED: SignUp Failed, Error message found.")
            






   
class SignUpPageTests(TestCase):
    # Acount Details
    def setUp(self):
        self.username = 'jonesuncle'
        self.password = '@uncle123'
        self.confirmPassword='@uncle123'
        self.email='AidenPearce@deadsec.com'
        self.user = User.objects.create_user(username=self.username, password=self.password)
     
      
    def test_GreetingMessgae(self):
        print(f"------------ ------------------ -------------")
        print(f"------------ TESTING SIGNUP PAGE--------------")
        print(f"-------- Test username: {self.username} ---------")
        print(f"-------- Test password: {self.password} --------")
        print(f"-------- Test confirm password: {self.confirmPassword} --------")
        print(f"-------- Test email: {self.email} --------")
        print(f"------------ ------------------ -------------")
        

    def test_SignUp_WrongEmail(self):
        """Show that If users inputs wrong emails it will throw an error"""
        print(f" ")
        print(f"                            TEST                                  ")
        print(f"Testing that If users inputs wrong emails it will throw an error")
        print(f"Test username: {self.username} Test password: badPassword ")
        print(f" ")
        
        response = self.client.post(reverse('vendor:signup'), {
            'username': self.username,
            'password1': self.password,
            'password2': 'self.confirmPassword',
            'email': self.email,
            'confirm password': self.password,
        })
        
        # login form should show this message if the logins dont match
        self.assertContains(response, "The two password fields didn’t match.")
        print(f"                            RESULT                                 ")
        print("TEST PASSED: SignUp Failed, Error message found.")
        
    def test_SignUp_EmptyForm(self):
        """Show that If the fields are empty it will throw an error"""
        print(f" ")
        print(f"                            TEST                                  ")
        print(f"Testing that If the fields are empty emails it will throw an error")
        print(f"Test username: Test password: ")
        print(f" ")
        
        response = self.client.post(reverse('vendor:signup'), {
            'password1': self.password,
            'password2': 'self.confirmPassword',
            'email': self.email,
            'confirm password': self.password,
        })
        
        # login form should show this message if the fields are empty
        self.assertContains(response, "This field is required")
        print(f"                            RESULT                                 ")
        print("TEST PASSED: SignUp Failed, Error message found.")
        