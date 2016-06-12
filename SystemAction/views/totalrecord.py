# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
# Create your views here.


from SystemAction.forms import SaveForm

# def index(request):
#     pass
#     return render_to_response('SystemAction/save.html',locals(),RequestContext(request))
#

@login_required()
@PermissionVerify()
def TotalRecord(request):
    from SystemAction.models import Record
    recordList = Record.objects.all()


    kwvars={
        'request':request,
        'recordlist':recordList,
    }

    return render_to_response('SystemAction/TotalRecord.html',kwvars,RequestContext(request))
    #return render(request,'SystemAction/save.html',{'form':form})
