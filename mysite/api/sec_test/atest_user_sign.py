import time
import hashlib
import requests

# &Guest-Bugmaster
client_time_ = str(time.time()).split(".")[0]
client_time = str(int(client_time_)-1)
sign_str = client_time + "&Guest-Bugmaster"
print(client_time)


md5 = hashlib.md5()
sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
md5.update(sign_bytes_utf8)
client_sign = md5.hexdigest()
print(client_sign)

base_url = "http://127.0.0.1:8000/api/user_sign"
data={"time": client_time, "sign": client_sign}
r = requests.post(base_url, data=data)
print(r.text)
