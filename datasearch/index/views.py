from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def datatables(request):
    
    username = request.GET.get('username','')
    if username is not None:
        is_login=True
    
    return render(request,'index.html',{'username':username,'is_login':is_login})
