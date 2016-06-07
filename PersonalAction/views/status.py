# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from UserManage.models import User
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from PersonalAction.models import Borrow
from SystemAction.models import Book
from django.http import HttpResponse
# Create your views here.

@login_required()
@PermissionVerify()
def Status(request):
    user = request.user
    borrowlist = Borrow.objects.filter(user=user)
    booklist =list()
    for b in borrowlist:
        booklist.append(b.book)

    kwvars={
        'request':request,
        'booklist':booklist,
    }

    return render_to_response('PersonalAction/status.html',kwvars,RequestContext(request))



@login_required()
@PermissionVerify()
def ReturnBook(request,book_id):
    from PersonalAction.models import Borrow

    #修改Book对象
    oneBook=Book.objects.get(book_id=book_id)
    oneBook.remain_num=oneBook.remain_num+1
    oneBook.save()
    #修改Borrow对象
    oneToRurn = Borrow.objects.filter(book=oneBook)
    oneToRurn.return_data

    pass