# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

from SystemAction.models import Book


@login_required()
@PermissionVerify()
def BookManage(request):

    booklist = Book.objects.all()

    kwvars={
        'request':request,
        'booklist':booklist
    }

    return render_to_response('SystemAction/bookmanage.html',kwvars,RequestContext(request))


@login_required()
@PermissionVerify()
def DelBook(request,book_id):

    delone = Book.objects.get(book_id=book_id)
    Book.delete(delone)

    return HttpResponseRedirect(reverse('bookmanage'))
