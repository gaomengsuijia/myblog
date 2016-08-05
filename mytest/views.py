
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import addForm
# Create your views here.

def hello(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))



def index(request):
	return render_to_response('index.html')


def add(request,a,b):
	a = int(a)
	b = int(b)
	c = a + b
	return HttpResponse(str(c))

def old_add_redict(request):
	return HttpResponseRedirect(
		reverse('tiao')
	)



def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )	

def test(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['username']
            b = form.cleaned_data['password']
            return HttpResponse(str(int(a) + int(b)))
    else:
    	form = AddForm()
	return render_to_response('test.html',{'form':form})
