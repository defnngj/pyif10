import requests

base_url = "http://127.0.0.1:8000/api/user_sign"
r = requests.get(base_url, auth=("admin", "admin123456"))
print(r.json())
