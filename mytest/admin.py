#coding:utf-8
from django.contrib import admin
from .models import Article

# Register your models here.
#显示更多的字段内容
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)





admin.site.register(Article)