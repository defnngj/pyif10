import os
import json
from django.forms.models import model_to_dict
from api.common import ApiResponse
from api.models import User
from mysite.settings import BASE_DIR


def hello(request):
    """
    最简单的json格式返回
    :param request:
    :return:
    """
    return ApiResponse(status=100, message="Welcome to API testing")


def user(request, uid):
    """
    RESTful 风格的接口实现
    实现用户的查询、添加、更新和删除
    /event/1/  = GET
    /event/2/  = POST
    /event/1/  = PUT
    /event/1/  = DELETE
    :param request:
    :param uid:
    :return:
    """
    if request.method == "GET":
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return ApiResponse(101, "用户信息不存在")
        else:
            user_info = model_to_dict(user)
            return ApiResponse(200, data=user_info)

    elif request.method == "POST":
        post = json.loads(request.body)
        name = post.get("name")
        age = post.get("age")
        try:
            User.objects.get(id=uid)
        except User.DoesNotExist:
            user = User.objects.create(id=uid, name=name, age=age)
            user_info = model_to_dict(user)
            return ApiResponse(message="add success", data=user_info)
        else:
            return ApiResponse(102, "用户id已存在")

    elif request.method == "PUT":
        put = json.loads(request.body)
        name = put.get("name")
        age = put.get("age")
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return ApiResponse(101, "用户信息不存在")
        else:
            user.name = name
            user.age = age
            user.save()
            user_info = model_to_dict(user)
            return ApiResponse(message="update success", data=user_info)

    elif request.method == "DELETE":
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return ApiResponse(101, "用户信息不存在")
        else:
            user.delete()
            return ApiResponse(message="delete success")
    else:
        return ApiResponse(100, message="请求方法错误")


def post_req(request):
    """
    post请求的几种参数：
    添加用例
    :param request:
    :return:
    """
    if request.method == "POST":
        print("request==>", request.body)
        # form-data 和  x-www-from-urlencode:
        name = request.POST.get("name", "")
        print("name-->", name)
        # JSON
        body = json.loads(request.body)
        name = body.get("name")
        print("json-name-->", name)

        return ApiResponse(status=200, message="successful")


def header(request):
    """
    获取 请求头Header的数据
    :param request:
    :return:
    """
    print("header => ",type(request.headers), request.headers)
    ct = request.headers["Content-Type"]
    token = request.headers["Token"]
    print("ct--->", ct)
    print("token--->", token)

    return ApiResponse(status=200, message="successful")


def upload_file(request):
    """
    实现文件上传
    :param request:
    :return:
    """
    if request.method == "POST":
        f = request.FILES.get("file")
        print("文件对象", type(f), f)
        print("文件name", f.name)
        file_name = f.name
        ff = file_name.split(".")[-1]
        print(ff)
        print("文件大小=》", f.size)
        if ff == "exe" or ff == "js":
            return ApiResponse(status=102, message="不支持这种类型的上传")

        # 保存上传的文件
        upload_dir = os.path.join(BASE_DIR, "api/upload")
        print(upload_dir)
        destination = open(os.path.join(upload_dir, file_name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in f.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
    return ApiResponse(status=200, message="successful")




"""
none: 
b''

form-data:
b'----------------------------
840552381995255595827715\r\nContent-Disposition: 
form-data; 
name="limit"\r\n\r\n1234123\r\n----------------------------
840552381995255595827715--\r\n'

x-www-from-urlencode:
b'name=huawei'

raw => text :
b'name=hello'

raw => JSON:
b'{\n\t"name": "hello"\n}'

raw => XML:
b'<xml>\n\t<name>hello</name>\n</xml>'


http 参数的格式有哪几种？

post : 参数的格式。json, form-data


/get_event_by_id/?eid=10  = GET
/add_event/   POST
{

}

/update_event/   POST
{

}
/delete_event/?eid=1  GET



RESTful 风格

查询
/event/1/  = GET
/event/2/    = POST
/event/1/  = PUT
/event/1/  = DELETE

"""