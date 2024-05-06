from django.shortcuts import render
from django.http import HttpResponse

def users(Req):
    return (HttpResponse("This Message Appears From Users Section"))
