# coding=utf-8
from django.db import models
from UserManage.models import User
from SystemAction.models import Book



# 借书表
class Borrow(models.Model):

    borrow_id = models.CharField(max_length=50,primary_key=True,null=False)
    #外键
    user= models.ForeignKey(User)
    #外键
    book= models.ForeignKey(Book)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.CharField(max_length=50,null=True)
    term_day = models.IntegerField(default=60)


