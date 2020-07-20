from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def login(request):
    return HttpResponse('login')

def safeB(request):
    return HttpResponse('实现了安全等级为B的级别')