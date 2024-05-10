from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
def playerName(req):
    template = loader.get_template('names.html')
    users = models.userGameInfos.objects.all().values()
    context = {
        'players': users
    }
    return (HttpResponse(template.render(context, req)))

def informations(req, id):
    template = loader.get_template('info.html')
    infos = models.userGameInfos.objects.get(id=id)
    context = {
        'profile': infos
    }
    return (HttpResponse(template.render(context, req)))