from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User


class LoginTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = Chrome()
        cls.selenium.implicitly_wait(10)

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        #super().tearDownClass()

    def test_login_null(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('')
        self.selenium.find_element_by_id('login_button').click()
        sleep(2)

    def test_login_error(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('error')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('error')
        self.selenium.find_element_by_id('login_button').click()
        sleep(2)

    def test_login_success(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('admin123456')
        self.selenium.find_element_by_id('login_button').click()
        sleep(2)
