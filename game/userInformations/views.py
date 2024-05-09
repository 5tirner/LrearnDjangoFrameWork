from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

def userDetails(req):
    template = loader.get_template('index.html')
    players = models.personalInfos.objects.all().values()
    context = {
        'players': players,
    }
    return (HttpResponse(template.render(context, req)))