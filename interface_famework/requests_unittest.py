import requests
import unittest
from ddt import ddt, data, unpack


@ddt
class DDTUsed(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api"

    @data(["xiaomi11 event", "beijing", 5000, "", 10101, "必传参数为空！"],
          ["xiaomi11 event", "beijing", 5000, "2010", 10102, "日期格式错误"],
          ["xiaomi11 event", "beijing", 5000, "2019-12-12 12:00:00", 10200, "创建发布会成功"],
          )
    @unpack
    def test_add_event(self, name_, address_, limit_, start_time_, status_, message_):
        data = {"name": name_, "address": address_,
                "limit": limit_, "start_time": start_time_
                }
        r = requests.post(self.base_url + "/add_event/", data=data)
        self.status_code = r.status_code
        result = r.json()
        print(result)
        self.assertEqual(result["status"], status_)
        self.assertEqual(result["message"], message_)


class MyTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api"

    def test_hello_api(self):
        r = requests.get(self.base_url + "/hello_api/")
        self.status_code = r.status_code
        result = r.json()
        self.assertEqual(result["status"], 10200)
        self.assertEqual(result["message"], "success")
        self.assertEqual(result["data"]["id"], 2)

    def test_get_event_id(self):
        r = requests.get(self.base_url + "/get_event_by_id/", params={"eid": 2})
        self.status_code = r.status_code
        result = r.json()
        print(result)
        self.assertEqual(result["status"], 10200)
        self.assertEqual(result["message"], "success")
        self.assertEqual(result["data"]['name'], "红米8发布会")

    def tearDown(self):
        self.assertEqual(self.status_code, 200)


if __name__ == '__main__':
    unittest.main()
