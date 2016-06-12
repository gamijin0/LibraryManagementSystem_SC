#coding: utf-8
from django.db import models
from UserManage.models import User

# Create your models here.
# 书籍信息
class Book(models.Model):
    book_id = models.CharField(max_length=20,primary_key=True,null=False)
    book_name = models.CharField(max_length=50,null=False)
    author = models.CharField(max_length=50,null=False)
    press = models.CharField(max_length=50,null=False)
    publication_year = models.SmallIntegerField(max_length=6,null=False)
    introduction = models.CharField(max_length=1000)
    add_time = models.DateField(auto_now_add=True)
    category_id = models.CharField(max_length=20,null=False)
    inventory = models.SmallIntegerField(max_length=4,null=False)
    remain_num = models.IntegerField(max_length=4,null=False,default=0)

class Record(models.Model):
    record_id = models.CharField(max_length=50,primary_key=True,null=False)
    user = models.ForeignKey(User)
    record_date = models.DateTimeField(auto_now_add=True,null=False)
    #category:[editbook,deletebook,savebook,borrowbook,returnbook,login]
    record_category = models.CharField(max_length=20,null=False)
    record_introduct = models.CharField(max_length=1000)