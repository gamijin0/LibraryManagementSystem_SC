# coding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render
from django.shortcuts import HttpResponse,render,render_to_response,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from SystemAction.views.savebook import SaveForm
from SystemAction.models import Book
from SystemAction.models import Record
from django.utils import timezone


@login_required()
@PermissionVerify()
def Borrow(request):
    from PersonalAction.models import Borrow as BorrowModule



    # 服务器请求函数
    booklist = Book.objects.all()

    bookBeBorrowed = BorrowModule.objects.filter(user=request.user).exclude(return_date=None)


    kwvars={
        'request':request,
        'booklist':booklist
    }

    return render_to_response('PersonalAction/borrow.html',kwvars,RequestContext(request))


def ChenkRemain(user,book_id):
    from PersonalAction.models import Borrow

    valid = True
    erros = list()

    bookBeBorrowedlist=Borrow.objects.filter(user=user,return_date=None)
    if(len(bookBeBorrowedlist)>=4):
        erros.append("超出借书数量限制.")
        valid=False

    if(Book.objects.get(book_id=book_id).remain_num<=0):
        erros.append("此书库存不足.")
        valid=False

    return {'valid':valid,'errors':erros}

def BorrowBook(request,book_id):
    # 查询数据库内对象
    res = ChenkRemain(request.user,book_id)
    if (res['valid'] == True):
        # 修改Book对象
        oneToSave = Book.objects.get(book_id=book_id)
        oneToSave.remain_num = oneToSave.remain_num - 1
        oneToSave.save()
        # 存入Borrow对象
        import datetime
        from PersonalAction.models import Borrow
        from UserManage.models import User
        from django.utils import timezone
        oneToBorrow = Borrow(
            borrow_id= str(request.user.id) + str(timezone.now())[:-6].replace(':','-').replace('.','-').replace(' ','-')
        )
        oneToBorrow.user = request.user
        oneToBorrow.book = oneToSave
        oneToBorrow.save()
        # 添加对应的操作记录
        oneRecord = Record(record_id=(
            "Re_" + str(request.user.id) + "_" + str(request.user.id) + str(timezone.now())[:-6].replace(':',
                                                                                                         '-').replace(
                '.', '-').replace(' ', '-')),
            user=request.user, record_category="borrowbook",
            record_introduct=u"用户[" + request.user.username +u"]借阅了书籍[" + oneToSave.book_name + "]"
        )
        oneRecord.save()
        # 存储成功后跳转到借书页面
        return HttpResponseRedirect(reverse('status'))
    else:
        return HttpResponse(str(res['errors']))
