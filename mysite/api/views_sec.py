import time
import base64
import hashlib
import json
from django.contrib import auth
from api.common import ApiResponse
from Crypto.Cipher import AES

# 用户认证
def user_auth(request):
    """
    用户认证
    """
    if request.method == "GET":
        auth_str = request.META["HTTP_AUTHORIZATION"]
        auth_ = base64.b64decode(auth_str.split(" ")[1])
        user_ = auth_.decode().split(":")[0]
        pawd_ = auth_.decode().split(":")[1]
        print(user_)
        print(pawd_)
        user = auth.authenticate(username=user_, password=pawd_)
        if user is None:
            return ApiResponse(102, "认证失败")

        return ApiResponse(200, "认证通过")

    else:
        return ApiResponse(101, "请求方法错误")


# 用户签名+时间戳
def user_sign(request):
    print(request.method)

    if request.method == 'POST':

        client_time = request.POST.get('time', '')   # 客户端时间戳
        client_sign = request.POST.get('sign', '')   # 客户端签名

        if client_time == '' or client_sign == '':
            return ApiResponse(102, "sign null")

        # 服务器时间
        server_time = str(time.time()).split('.')[0]
        print("客户端端时间:", client_time)
        print("服务器端时间:", server_time)

        # 获取时间差
        time_difference = int(server_time) - int(client_time)
        if time_difference >= 3:
            return ApiResponse(102, "timeout")

        # 签名检查
        md5 = hashlib.md5()
        sign_str = client_time + "&Guest-Bugmaster"
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        sever_sign = md5.hexdigest()

        print("客户端端签名:", client_sign)
        print("服务器端签名:", sever_sign)

        if sever_sign != client_sign:
            return ApiResponse(103, "sign fail")
        else:
            return ApiResponse(200, "sign success", data={"password": "admin123456"})

    else:
        return ApiResponse(101, "请求方法错误")


# =======AES加密算法===============
BS = 16
unpad = lambda s: s[0: - ord(s[-1])]


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)


def decryptAES(src):
    """解析AES密文"""
    print(src)
    src_aes = decryptBase64(src)
    print(src_aes)
    key = b'W7v4D60fds2Cmk2U'
    iv = b"1172311105789011"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    text = cryptor.decrypt(src_aes).decode()
    return unpad(text)


def user_aes(request):
    if request.method == 'POST':
        data = request.POST.get("data", "")
        if data == "":
            return ApiResponse(102, "data null")

        # 解密
        decode = decryptAES(data)

        # 转化为字典
        dict_data = json.loads(decode)
        print(dict_data)

        return ApiResponse(200, "success")

    else:
        return ApiResponse(101, "请求方法错误")
