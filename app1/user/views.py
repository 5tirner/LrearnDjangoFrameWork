from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def user(req):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    return HttpResponse("Five")
