# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render
from django.shortcuts import HttpResponse,render,render_to_response,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from SystemAction.views.savebook import SaveForm
from SystemAction.models import Book



@login_required()
@PermissionVerify()
def BookManage(request):
    # 提取书籍信息
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

def Borrow(requests):
    pass
