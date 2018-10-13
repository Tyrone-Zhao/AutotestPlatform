from django.contrib import admin
from bug.models import Bug


class BugAdmin(admin.ModelAdmin):
	list_display = ["bugname", "bugdetail", "bugstatus", "buglevel", "bugcreater", "bugassign", "create_time", "id"]

admin.site.register(Bug)  # 把Bug管理模块注册到Django admin后台并能显示