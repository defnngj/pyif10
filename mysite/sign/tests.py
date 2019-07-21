from django.test import TestCase
from sign.models import Event, Guest
from django.contrib.auth.models import User


# Create your tests here.
class EventTestCase(TestCase):

    def setUp(self):
        Event.objects.create(name="xiaomi8", limit="2000", status=True,
        address="beijing", start_time="2019-11-11 14:00:00")

    def test_select(self):
        """查询"""
        event = Event.objects.get(name="xiaomi8")
        print(len(event))
        self.assertEqual(event.address, 'beijing')
    
    def test_update(self):
        """更新"""
        event = Event.objects.get(name="xiaomi8")
        event.address = "shanghai"
        event.save()
        event = Event.objects.get(name="xiaomi8")
        self.assertEqual(event.address, "shanghai")

    def test_add(self):
        """添加"""
        Event.objects.create(name="huawei20", limit="5000", status=True, 
        address="上海", start_time="2019-12-11 14:00:00")
        event = Event.objects.get(name="huawei20")
        self.assertEqual(event.limit, 5000)

    def test_delete(self):
        """删除"""
        event = Event.objects.get(name="xiaomi8")
        event.delete()
        event = Event.objects.filter(name="xiaomi8")
        self.assertEqual(len(event), 0)


class HelloViewTest(TestCase):

    def test_hello(self):
        response = self.client.get("/hello")
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hello.html")


class LoginViewTest(TestCase):

    def setUp(self):
        #Event.objects.create()
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_login_null(self):
        user = {'username': '', 'password': ''}
        resp = self.client.post("/login", user)
        #print(resp.status_code)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "index.html")
        self.assertIn(b"username or password null", resp.content)

    def test_login_error(self):
        user = {'username': 'error', 'password': 'error'}
        resp = self.client.post("/login", user)
        #print(resp.status_code)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "index.html")
        self.assertIn(b"username or password error", resp.content)

    def test_login_success(self):
        user = {'username': 'admin', 'password': 'admin123456'}
        resp = self.client.post("/login", user)
        print(resp.status_code)
        print(resp.content)
        self.assertEqual(resp.status_code, 302)


class ManageViewTest(TestCase):

    def setUp(self):
        Event.objects.create(name="xiaomi8", limit="2000", status=True,
                             address="beijing", start_time="2019-11-11 14:00:00")
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        user = {'username': 'admin', 'password': 'admin123456'}
        resp = self.client.post("/login", user)

    def test_manage_page(self):
        resp = self.client.get("/manage")
        print(resp.status_code)
        print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "event_mange.html")
        self.assertIn(b"xiaomi8", resp.content)
