# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from UserManage.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from PersonalAction.models import Borrow
from SystemAction.models import Book
from django.http import HttpResponse,HttpResponseRedirect
from SystemAction.models import Record
from django.utils import timezone
# Create your views here.

@login_required()
@PermissionVerify()
def Status(request):
    user = request.user

    borrowlist = Borrow.objects.filter(user=user,return_date=None)

    kwvars={
        'request':request,
        'borrowList':borrowlist,
    }

    return render_to_response('PersonalAction/status.html',kwvars,RequestContext(request))



@login_required()
@PermissionVerify()
def ReturnBook(request,borrow_id):
    from PersonalAction.models import Borrow
    from django.utils import timezone
    import datetime

    oneToReturn=Borrow.objects.get(borrow_id=borrow_id)
    oneToReturn.return_date= timezone.now()
    oneToReturn.book.remain_num+=1
    oneToReturn.book.save()
    oneToReturn.save()
    # 添加对应的操作记录
    oneRecord = Record(record_id=(
        "Re_" + str(request.user.id) + "_" + str(request.user.id) + str(timezone.now())[:-6].replace(':',
                                                                                                     '-').replace(
            '.', '-').replace(' ', '-')),
        user=request.user, record_category="returnbook",
        record_introduct=u"用户[" + request.user.username +u"]归还了书籍[" + oneToReturn.book.book_name + "]"
    )
    oneRecord.save()

    return HttpResponseRedirect(reverse("status"))