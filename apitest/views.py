from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login


def test(request):
	return HttpResponse("hello test")  # 返回HttpResponse响应函数


def login(request):
	if request.POST:
		username = password = ""
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			request.session["user"] = username
			response = HttpResponseRedirect("/home/")
			return response
		else:
			return render(request, "login.html", 
				{"error": "username or password error"})
	# else:
		# context = {}
		# return render(request, "login.html", context)

	return render(request, "login.html")


def home(request):
	return render(request, "home.html")