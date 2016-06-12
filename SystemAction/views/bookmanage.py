# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from SystemAction.views.savebook import SaveForm
from SystemAction.models import Book
from SystemAction.models import Record
from django.utils import timezone



@login_required()
@PermissionVerify()
def BookManage(request):
    # 修改书籍信息
    if(request.method=="POST"):

        #print(request.POST)

        res=ChenkValid(request.POST)
        if(res['valid']==True):
            #表单有效
            pass
            # 查询数据库内对象
            oneToEdit = Book.objects.get(book_id=request.POST['book_id'])
            oneToEdit.author=request.POST['author']
            oneToEdit.book_name = request.POST['book_name']
            oneToEdit.category_id = request.POST['category_id']

                #计算新增数量
            addedCounts = int(request.POST['inventory'])-oneToEdit.inventory
            oneToEdit.inventory = int(request.POST['inventory'])
            oneToEdit.remain_num = oneToEdit.remain_num+addedCounts
            oneToEdit.save()

            oneRecord=Record(record_id=("Re_"+str(request.user.id)+"_"+str(request.user.id) + str(timezone.now())[:-6].replace(':','-').replace('.','-').replace(' ','-')),
                             user=request.user,
                             record_category="editbook",
                             record_introduct=u"用户["+request.user.username+u"]修改了书籍["+oneToEdit.book_name+u"]的信息")
            oneRecord.save()
        else:
            #表单中有错误
            return HttpResponse(str(res['errors']))

        # 存储成功后跳转到图书管理页面
        return HttpResponseRedirect(reverse('bookmanage'))


    else:
        # 服务器请求函数
        booklist = Book.objects.all()

        kwvars={
            'request':request,
            'booklist':booklist
        }

        return render_to_response('SystemAction/bookmanage.html',kwvars,RequestContext(request))


@login_required()
@PermissionVerify()
def DelBook(request,book_id):
    # 删除书籍函数
    delone = Book.objects.get(book_id=book_id)
    Book.delete(delone)

    oneRecord = Record(record_id=(
        "Re_" + str(request.user.id) + "_" + str(request.user.id) + str(timezone.now())[:-6].replace(':', '-').replace('.','-').replace(' ', '-')),
        user=request.user,record_category="deletebook",
        record_introduct=u"用户[" + request.user.username + u"]删除了书籍[" +delone.book_name+ "]"
    )
    oneRecord.save()

    return HttpResponseRedirect(reverse('bookmanage'))


def ChenkValid(POST):

    valid = True
    erros = list()

    import datetime
    if(POST['publication_year']<1800 or int(POST['publication_year'])>int(str(datetime.date.today())[0:4])):
        erros.append("Invalid publication_year")
        valid=False

    return {'valid':valid,'errors':erros}
