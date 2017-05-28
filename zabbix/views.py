from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.shortcuts import HttpResponse
import os
from zabbix import models

def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        print(u,p)
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            return redirect('index.html',{'user_obj': obj})
        else:
            render(request,'login.html')
    else:
        # PUT,DELETE,HEAD,OPTION...
        return render(request, 'login.html')



def orm(request):
    #插入数据
    # models.UserInfo.objects.create(username='root', password='123')

    #删除数据
    # models.UserInfo.objects.filter(username='root').delete()

    #改数据
    # models.UserInfo.objects.filter(password=123).update(username='root4')

    #查数据
    result = models.UserInfo.objects.filter(username='root2')
    for row in result:
        u,p=row.username,row.password
        print(u,p)


def index(request):
    return render(request,'index.html')
