from django.db import models

#Event.objects.create(name="小米8发布会", limit=2000, status=True, address="北京", start_time="2019-12-12 14:00:00")
# event = Event.objects.get(id=1)
#
# Guest.objects.create(realname="张三", phone="18611001100", email="zhangsan@mail.com", sign=False, event=event)
#
# Guest.objects.create(realname="李四", phone="18611001100",email="lisi@mail.com", sign=False, event_id=1)
# Guest.objects.select_for_update().filter(phone='13611001101').update(realname='andy')
#
# Guest.objects.select_for_update().filter(id=1).update(realname="张三")


# Create your models here.
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



# 创建数据库表的， ORM  对象关系映射

# select * from user where username=my_username and password=my_password;

# python  -->  驱动（pymysql）-->  mysql
# sqlit3
# python  --> ORM(models.py) --> 驱动（PyMySQL）--> mysql

# 数据库： 表、id(inter, max=10)，name("tom"),datetime...
# select * from user where username;
#
#
# class User():
#     id = Int(max=10,)
#     name = char(def="tom")
#     datatime =
#     ..
#
# User.object.all()
# User.object.get(username="tom", password="123")


# 发布会签到系统
# 发布会表
# 小米8 发布会： 名称、人数、状态、时间、地址、id、创建时间
# 小米9发布会
#
# 嘉宾表：
# 张三：名称、邮箱、手机号、签到状态、id、创建时间，发布会8
# 张三：名称、邮箱、手机号、签到状态、id、创建时间，发布会9
#
#







