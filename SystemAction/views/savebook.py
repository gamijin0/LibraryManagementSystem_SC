# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

from SystemAction.forms import SaveForm


@login_required()
@PermissionVerify()
def SaveBook(request):
    from SystemAction.models import Book
    if (request.method=='POST'):#有提交请求

        form = SaveForm(request.POST)
        if(form.is_valid()):

            #构造数据库对象
            oneToSave = Book(
                book_id=form.cleaned_data['book_id'],
                book_name=form.cleaned_data['book_name'],
                author=form.cleaned_data['author'],
                press=form.cleaned_data['press'],
                publication_year=form.cleaned_data['publication_year'],
                category_id=form.cleaned_data['category_id'],
                inventory=form.cleaned_data['inventory'],
                remain_num=form.cleaned_data['remain_num'],
                )
            #存入数据库
            oneToSave.save()
            #存储成功后跳转到图书管理页面
            return HttpResponseRedirect(reverse('bookmanage'))

    else:
        form = SaveForm()
        kwvars={
            'form':form,
            'request':request,
        }
        return render_to_response('SystemAction/save.html',kwvars,RequestContext(request))

    return render_to_response('SystemAction/save.html',{'form':form,'request':request},RequestContext(request))
