# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext,render
def FineRule(request):
    return render_to_response('Other/Fine.html',RequestContext(request))