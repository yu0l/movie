from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse
import json


# def app02_re1(request):
#     return HttpResponse("呵呵")

def app02_re1(request):
    today = datetime.now()
    format_date = today.strftime('%Y-%m-%d')
    html = (f'<html><h5>今天是{format_date}</h5></html>')
    return HttpResponse(html)
