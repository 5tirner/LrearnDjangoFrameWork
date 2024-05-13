from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models
def start(req):
    template = loader.get_template('start.html')
    return (HttpResponse(template.render()))
def names(req):
    template = loader.get_template('names.html')
    users = models.infos.objects.all().values()
    context = {
        'usr': users
    }
    return HttpResponse(template.render(context, req))