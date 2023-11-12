from django.http import HttpResponse,JsonResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login_template(request):       
    template = loader.get_template('logreg.html')
    return HttpResponse(template.render())

@csrf_exempt
def login_view(request):
    if request.method=="POST":
        data = json.loads(request.body.decode())
        
        username=data["username"]
        password=data["password"]
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            request.session['user_authenticated'] = True
            request.session['username'] = username
            return JsonResponse({"error_code":0,"msg":"登陆成功"})
        else:
            return JsonResponse({"error_code":1,"msg":"用户名或密码错误"})
    else:
        return HttpResponse("这是登录页面。")        
    
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        # 解析JSON数据
        data = json.loads(request.body.decode())
        username=data["username"]
        password=data["password"]
        inviteCode=data["inviteCode"]
        if inviteCode == "UntermRad":
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({"error_code": 0, "msg": "注册成功"})
        else:
            return JsonResponse({"error_code": 1, "msg": "注册失败"})
    else:
        return HttpResponse("这是注册页面。")