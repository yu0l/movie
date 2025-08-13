from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return HttpResponse("helloworld!")
def index(request,year,mounth):
    return HttpResponse(f"{year}年{mounth}月所有文章")