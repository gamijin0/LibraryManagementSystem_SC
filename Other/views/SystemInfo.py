# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext,render
def SystemInfor(request):
    return render_to_response('Other/Infor.html',RequestContext(request))