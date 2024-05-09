from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

def welcomeFunction(req):
    myWords = models.table1.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myWords': myWords,
    }
    return (HttpResponse(template.render(context, req)))
