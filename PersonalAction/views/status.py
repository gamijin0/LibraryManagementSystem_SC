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
    import datetime

    oneToReturn=Borrow.objects.get(borrow_id=borrow_id)
    oneToReturn.return_date= datetime.datetime.today()
    oneToReturn.book.remain_num+=1
    oneToReturn.book.save()
    oneToReturn.save()

    return HttpResponseRedirect(reverse("status"))