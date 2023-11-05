from django.http import HttpResponse
from django.template import loader

def login(request):
    template = loader.get_template('logreg.html')
    return HttpResponse(template.render())

def regist(request):
    template = loader.get_template('logreg.html')
    return HttpResponse(template.render())
