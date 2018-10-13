from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from apptest.models import Appcase, Appcasestep


# app用例管理
@login_required
def appcase_manage(request):
	appcase_list = Appcase.objects.all()
	username = request.session.get("user", "")  # 读取浏览器登录Session
	return render(request, "appcase_manage.html", {"user": username, "appcases": appcase_list})


# App用例测试步骤
@login_required
def appcasestep_manage(request):
	username = request.session.get("user", "")
	appcasestep_list = Appcasestep.objects.all()
	return render(request, "appcasestep_manage.html", {"user": username, "appcasesteps": appcasestep_list})