from django.contrib import admin
from product.models import Product
from apitest.models import Apitest, Apis


class ProductAdmin(admin.ModelAdmin):
	list_display = ["productname", "productdesc", "producter", "create_time", "id"]


admin.site.register(Product, ProductAdmin)  # 把产品模块注册到Django admin后台并能显示



class ApisAdmin(admin.TabularInline):
	list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id', 'product']
	model = Apis
	extra = 1


class ProductAdmin(admin.ModelAdmin):
	list_display = ['productname', 'productdesc', 'create_time', 'id']
	inlines = [ApisAdmin]
		