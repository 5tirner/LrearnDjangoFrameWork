from django.shortcuts import render
from django.http import HttpResponse

def users(req):
    return HttpResponse("Hi Users")
