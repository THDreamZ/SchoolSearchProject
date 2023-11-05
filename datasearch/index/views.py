from django.template import loader
from django.http import HttpResponse

def datatables(request):
    tempalte = loader.get_template('index.html')
    return HttpResponse(tempalte.render())