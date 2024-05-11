from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

def name(req):
    template = loader.get_template('name.html')
    usr = models.usrInfo.objects.all().values()
    context = {
        'u': usr,
    }
    return (HttpResponse(template.render(context, req)))

def info(req, id):
    usr = models.usrInfo.objects.get(id=id)
    template = loader.get_template('info.html')
    context = {
        'u': usr,
    }
    return (HttpResponse(template.render(context, req)))