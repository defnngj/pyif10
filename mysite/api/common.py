from django.http import JsonResponse


class Response:

    # 返回成功
    def success(self, status=None, message=None, data=[]):
        if status is None:
            status = 10200
        if message is None:
            message = "success"

        response_dict = {
            "status": status,
            "message": message,
            "data": data
        }
        return JsonResponse(response_dict)

    def fail(self, status=None, message=None):

        if status is None:
            status__ = 10100
        else:
            status__ = 10100 + int(status)

        if message is None:
            message = "fail"

        response_dict = {
            "status": status__,
            "message": message
        }
        return JsonResponse(response_dict)

    # 请求方法错误
    @property
    def request_error(self, message="request method error"):
        return self.fail(message=message)
