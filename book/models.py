from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False, default=0)

    def __str__(self):
        # 设置打印格式（返回的对象）
        return "<Book:({name},{author},{price})>".format(name=self.name,
                                                         author=self.author,
                                                         price=self.price)


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)