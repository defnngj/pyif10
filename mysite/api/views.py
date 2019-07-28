from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from sign.models import Event


def hello_api(request):
    interface_data = {"statue": 10200,
                      "message": "success",
                      "data": {
                          "id": 123, "name": "tom"
                        }
                      }
    return JsonResponse(interface_data)


def get_events(request):
    """
    获取所有发布会数据 接口
    """
    if request.method == "GET":
        events = Event.objects.all()
        data_list = []
        for event in events:
            data_list.append(
                {
                    "id": event.id,
                    "name": event.name,
                    "start_time": event.start_time,
                    "address": event.address,
                    "status": event.status,
                }
            )
            print(event.name)
            print(event.start_time)
            print(event.address)

        return JsonResponse({"status": 10200,
                             "message": "success",
                             "data": data_list})
    else:
        return JsonResponse({"status": 10100,
                             "message": "request method error",
                             })


def get_event(request):
    """
    根据id,获取某一个发布会数据
    """
    if request.method == "GET":
        eid = request.GET.get("eid", "")
        print("eid", type(eid), eid)
        if eid == "":
            return JsonResponse({"status": 10102,
                                 "message": "eid is null",
                                 })

        try:
            int(eid)
        except ValueError:
            return JsonResponse({"status": 10103,
                                 "message": "eid is not int type",
                                 })

        try:
            event = Event.objects.get(id=eid)
        except Event.DoesNotExist:
            return JsonResponse({"status": 10101,
                                 "message": "Event matching query does not exist.",
                                 })
        data_dict = {
            "id": event.id,
            "name": event.name,
            "start_time": event.start_time,
            "address": event.address,
            "status": event.status,
        }
        return JsonResponse({"status": 10200,
                             "message": "success",
                             "data": data_dict})
    else:
        return JsonResponse({"status": 10100,
                             "message": "request method error",
                             })


"""
发布会：查询、添加、更新、删除
嘉宾：查询、添加、更新、删除
"""
