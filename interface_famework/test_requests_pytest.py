import requests
import pytest


@pytest.mark.parametrize(
    "name_, address_, limit_, start_time_, status_, message_",
    [
        ("xiaomi11 event", "beijing", 5000, "", 10101, "必传参数为空！"),
        ("xiaomi11 event", "beijing", 5000, "2010", 10102, "日期格式错误"),
        ("xiaomi11 event", "beijing", 5000, "2019-12-12 12:00:00", 10200, "创建发布会成功")
    ]
)
def test_add_event(base_url, name_, address_, limit_, start_time_, status_, message_):
    data = {"name": name_, "address": address_,
            "limit": limit_, "start_time": start_time_
            }
    r = requests.post(base_url + "/add_event/", data=data)
    result = r.json()
    print(result)
    assert result["status"] == status_
    assert result["message"] == message_


def test_hello_api(base_url):
    r = requests.get(base_url + "/hello_api/")
    result = r.json()
    assert result["status"] == 10200
    assert result["message"] == "success"
    assert result["data"]["id"] == 2


def test_get_event_id(base_url):
    r = requests.get(base_url + "/get_event_by_id/", params={"eid": 2})
    result = r.json()
    print(result)
    assert result["status"] == 10200
    assert result["message"] == "success"
    assert result["data"]['name'] == "红米8发布会"
