# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
# Create your views here.


from SystemAction.forms import SaveForm
@login_required()
@PermissionVerify()
def PersonalRecord(request):
    from SystemAction.models import Record
    recordList = Record.objects.filter(user=request.user)

    for item in recordList:
        if(item.record_category=="editbook" or item.record_category == "savebook" or item.record_category=="deletebook"):
            recordList.delete(item)

    kwvars={
        'request':request,
        'recordlist':recordList,
    }


    return render_to_response('PersonalAction/PersonalRecord.html',kwvars,RequestContext(request))
