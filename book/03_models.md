
### Django 创建表

在 ```models.py``` 文件中创建数据库表：

```python
from django.db import models


class Event(models.Model):
    """
    发布会表
    """
    name = models.CharField(max_length=100)            # 发布会标题
    limit = models.IntegerField()                      # 限制人数
    status = models.BooleanField()                     # 状态
    address = models.CharField(max_length=200)         # 地址
    start_time = models.DateTimeField('events time')   # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name


class Guest(models.Model):
    """
    嘉宾表
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)     # 手机号
    email = models.EmailField()                 # 邮箱
    sign = models.BooleanField()                # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.realname

```

数据类型查看 ```C:\Python37\Lib\site-packages\django\db\models\fields\__init__.py```

### 数据库表操作

* 创建

```python
Event.objects.create(name="小米8发布会", limit=2000, status=True, address="北京", start_time="2019-12-12 14:00:00")

```

* 查询

```python
Event.objects.all()
Event.objects.get(pk=1)
Event.objects.filter(status=1)
Event.objects.filter(name__contains='发布会')
```

* 更新

```python
#单条数据更新
g = Project.objects.get(name='xxx测试项目')
g.status=0
g.save()

# 批量更新
Project.objects.select_for_update().filter(name__contains='项目').update(describe='')
```

* 删除

```python
Project.objects.get(name='xxx测试项目').delete()
```

```python
Event.objects.create(name="小米8发布会", limit=2000, status=True, address="北京", start_time="2019-12-12 14:00:00")
event = Event.objects.get(id=1)

Guest.objects.create(realname="张三", phone="18611001100", email="zhangsan@mail.com", sign=False, event=event)
Guest.objects.create(realname="李四", phone="18611001100",email="lisi@mail.com", sign=False, event_id=1)
Guest.objects.select_for_update().filter(phone='13611001101').update(realname='andy')

Guest.objects.select_for_update().filter(id=1).update(realname="张三")
```