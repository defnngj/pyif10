### django实现登录

在 __index.html__ 页面当中:

```html
<form action="/login_action/" method="get/post">
    <input name="username">
    <input name="password">
</form>
```

* 请求路径 login/
* 请求方法：get/post
* input 标签的 name属性是传参的名称

在 __views.py__ 文件中：

```python 
from django.contrib import auth

def login(request):
    """实现登录功能"""
    if request.method == "GET":
        # 返回登录页面
        return render(request, "index.html")
    else:
        # 处理登录请求
        my_username = request.POST.get("username")
        my_password = request.POST.get("password")

        if my_username == "" or my_password == "":
            return render(request, "index.html", {"hint": "用户名或密码为空！"})

        user = auth.authenticate(username=my_username, password=my_password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect("/manage")
            # response.set_cookie('user', my_username, 3600) # 添加浏览器 cookie
            request.session['user2'] = my_username  # 添加 session
            return response
        else:
            return render(request, "index.html", {"hint": "用户名密错误！"})

```

* request.method 为GET请求，返回登录页面，否则处理用户登录。
* request.POST.get("username", "") 获取POST请求的参数。
* auth.authenticate 判断用户是否存在。
* auth.login(request, user)  保留用户的登录信息。
