# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from UserManage.models import User
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from PersonalAction.models import Borrow
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
def ReturnBook(request):
    pass