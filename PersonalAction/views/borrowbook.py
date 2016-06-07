# coding =utf-8
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
def Borrow(request):
    # 提取书籍信息
    if(request.method=="POST"):
            # 查询数据库内对象
        res =ChenkRemain(request.POST)
        if(res['valid']==True):
            oneToSave = Book.objects.get(book_id=request.POST['book_id'])
            oneToSave.remain_num = oneToSave.remain_num - 1
        # oneToSave.author=request.POST['author']
        # oneToSave.book_name = request.POST['book_name']
        # oneToSave.category_id = request.POST['category_id']

                #计算新增数量
        # addedCounts = int(request.POST['inventory'])-oneToSave.inventory
        # oneToSave.inventory = int(request.POST['inventory'])
        # oneToSave.remain_num = oneToSave.remain_num+addedCounts-1
            oneToSave.save()
        # 存储成功后跳转到借书页面
            return HttpResponseRedirect(reverse('borrow'))
        else:
            return HttpResponse(str(res['errors']))

    else:
        # 服务器请求函数
        booklist = Book.objects.all()

        kwvars={
            'request':request,
            'booklist':booklist
        }

        return render_to_response('SystemAction/borrow.html',kwvars,RequestContext(request))


def ChenkRemain(POST):

    valid = True
    erros = list()

    if(POST['remain_num']<=0):
        erros.append("There is no book to lend!")
        valid=False

    return {'valid':valid,'errors':erros}
