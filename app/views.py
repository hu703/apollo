from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def safeA(request):
    return HttpResponse('实现了A级别的安全等级')