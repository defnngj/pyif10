import requests
import json
import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def encryptBase64(src):
    """生成 base64 字符串"""
    return base64.urlsafe_b64encode(src)


def encryptAES(src):
    """生成AES密文"""
    key = b'W7v4D60fds2Cmk2U'
    iv = b"1172311105789011"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    src_str = pad(src)
    print(src, len(src))
    print(src_str, len(src_str))
    src_byte = src_str.encode('utf-8')
    ciphertext = cryptor.encrypt(src_byte)  # AES加密
    print(ciphertext)
    aes_base64 = encryptBase64(ciphertext)  # base64 二次加密
    print(aes_base64)
    return aes_base64


base_url = "http://127.0.0.1:8000/api/user_aes"
data = {"id": 1, "name": "tom"}

data_str = json.dumps(data)
data_aes = encryptAES(data_str).decode()
print(data_aes)

r = requests.post(base_url, data={"data": data_aes})
print(r.json())
