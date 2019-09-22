import time
from datetime import datetime
from sign.models import Event, Guest
from django.forms.models import model_to_dict
from django.core.exceptions import ValidationError
from api.common import Response


# 实现项目当中的系统 和 业务有关
def hello_api(request):
    interface_data2 = {"id": 2, "name": "tom"}
    return Response().success(data=interface_data2)


def get_events(request):
    """
    获取所有发布会数据 接口
    """
    if request.method == "GET":
        events = Event.objects.all()
        data_list = []
        for event in events:
            data_list.append(model_to_dict(event))

        return Response().success(data=data_list)

    else:
        return Response().request_error


def get_event_by_id(request):
    """
    根据id,获取某一个发布会数据
    """
    if request.method == "GET":
        eid = request.GET.get("eid", "")

        if eid == "":
            return Response().fail(2, "eid is null")

        try:
            int(eid)
        except ValueError:
            return Response().fail(3, "eid is not int type")

        try:
            event = Event.objects.get(id=eid)
        except Event.DoesNotExist:
            return Response().fail(1, "Event matching query does not exist.")

        return Response().success(data=model_to_dict(event))

    else:
        return Response().request_error


def get_event_by_name(request):
    """
    根据发布会的名称模糊查询
    """
    if request.method == "GET":
        name = request.GET.get("name", "")
        events = Event.objects.filter(name__contains=name)

        event_list = []
        for event in events:
            event_list.append(model_to_dict(event))

        return Response().success(data=event_list)
    else:
        return Response().request_error


def add_event(request):
    """添加发布会"""
    if request.method == "POST":
        name = request.POST.get("name", "")
        limit = request.POST.get("limit", "")
        status = request.POST.get("status", "")
        address = request.POST.get("address", "")
        start_time = request.POST.get("start_time", "")

        if (name == "" or limit == ""
                or address == "" or start_time == ""):
            return Response().fail(1, message="必传参数为空！")

        if status == "":
            status = 1

        try:
            Event.objects.create(name=name, limit=limit, status=status,
                                 address=address, start_time=start_time)
        except ValidationError:
            return Response().fail(2, message="日期格式错误")

        return Response().success(message="创建发布会成功")

    else:
        return Response().request_error


def update_event(request):
    """
    更新发布会数据
    """
    if request.method == "POST":
        eid = request.POST.get("eid", "")
        name = request.POST.get("name", "")
        limit = request.POST.get("limit", "")
        status = request.POST.get("status", "")
        address = request.POST.get("address", "")
        start_time = request.POST.get("start_time", "")

        if eid == "":
            return Response().fail(1, message="必传参数为空！")

        try:
            int(eid)
        except ValueError:
            return Response().fail(2, "eid is not int type")

        try:
            event = Event.objects.get(id=eid)
        except Event.DoesNotExist:
            return Response().fail(3, "Event matching query does not exist.")

        if name != "":
            event.name = name
        if limit != "":
            event.limit = limit
        if address != "":
            event.address = address
        if start_time != "":
            event.start_time = start_time
        if status != "":
            event.status = status
        event.save()

        return Response().success(message="发布会更新成功")

    else:
        return Response().request_error


def delete_event(request):
    """
    删除发布会接口
    """
    if request.method == "GET":
        eid = request.GET.get("eid", "")

        if eid == "":
            return Response().fail(1, message="eid参数为空！")

        try:
            int(eid)
        except ValueError:
            return Response().fail(2, "eid is not int type")

        try:
            event = Event.objects.get(id=eid)
        except Event.DoesNotExist:
            return Response().fail(3, "Event matching query does not exist.")

        event.delete()

        return Response().success(message="发布会删除成功")

    else:
        return Response().request_error


"""
发布会：查询、添加、更新、删除
嘉宾：查询、添加、更新、删除
"""


def guest_sign(request):
    """
    嘉宾签到 接口
    """
    if request.method == "POST":
        eid = request.POST.get("eid", "")
        phone = request.POST.get("phone", "")

        if eid == "" or phone == "":
            return Response().fail(1, message="eid或phone参数为空")

        try:
            int(eid)
        except ValueError:
            return Response().fail(2, "eid类型错误")

        try:
            event = Event.objects.get(id=eid)
        except Event.DoesNotExist:
            return Response().fail(3, "发布会不存在")
        else:
            if event.status == 0:
                return Response().fail(4, "发布会状态已关闭")

            this_date = datetime.strptime(str(event.start_time), '%Y-%m-%d %H:%M:%S')
            event_time = time.mktime(this_date.timetuple())

            event_time_int = int(str(event_time).split(".")[0])
            now_time = int(str(time.time()).split(".")[0])
            if event_time_int < now_time:
                return Response().fail(5, message="发布会已经结束")

        guest = Guest.objects.filter(phone=phone)
        if len(guest) == 0:
            return Response().fail(6, "签到的嘉宾不存在")

        guest = Guest.objects.filter(phone=phone, event_id=eid)
        if len(guest) == 0:
            return Response().fail(7, "嘉宾没有参加该发布会")

        guest = Guest.objects.get(phone=phone, event_id=eid)
        if guest.sign == 1:
            return Response().success(message="用户已经签到")
        else:
            guest.sign = 1
            guest.save()
            return Response().success(message="签到成功")

    else:
        return Response().request_error
