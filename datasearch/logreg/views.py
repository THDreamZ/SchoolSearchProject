from django.http import HttpResponse
from django.template import loader
import json

def login(request):
    if request.method=="POST":
        data = json.loads(request.body.decode())
        
        username=data["username"]
        password=data["password"]
        print(username,password)
        if username and password:
            username=username.strip()
            
    template = loader.get_template('logreg.html')
    return HttpResponse(template.render())

def regist(request):
    template = loader.get_template('logreg.html')
    return HttpResponse(template.render())
