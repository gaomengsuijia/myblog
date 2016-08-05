#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField(primary_key=True)



class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
 
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    #这个函数的作用是将默认的标题（英文）改为模型里面的真实样子
    def __unicode__(self):
    	return self.title
