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
    add_time = models.DateField(auto_now=True)
    category_id = models.CharField(max_length=20,null=False)
    inventory = models.SmallIntegerField(max_length=4,null=False)
    remain_num = models.IntegerField(max_length=4,null=False,default=0)


# 借书表
class Borrow(models.Model):

    borrow_id = models.CharField(max_length=20,primary_key=True,null=False)
    #外键
    user= models.ForeignKey(User)
    #外键
    book= models.ForeignKey(Book)
    borrow_date = models.DateField(auto_now=True)
    return_date = models.CharField(max_length=50,null=True)
    term_day = models.IntegerField(default=60)

