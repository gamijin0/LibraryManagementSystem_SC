# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse
# Create your views here.


def Status(request):
    pass
    return render(request,'PersonalAction/status.html')