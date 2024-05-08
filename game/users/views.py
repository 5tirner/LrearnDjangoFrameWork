from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

def User(req):
    playerList = models.userInformations.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'playerList' : playerList,
    }
    return HttpResponse(template.render(context, req))
   
