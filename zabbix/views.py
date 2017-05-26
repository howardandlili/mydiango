from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.shortcuts import HttpResponse


def login(request):
    #定义登陆方法
    error_mag = ''#定于错误信息初始化话
    #在这里request会获得所有的用户信息~我们要把他分成get和post
    if request.method == 'POST': #这里记得是大写
        #当是post的 时候就是传过来账号密码
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'hy' and pwd == '123':
            return redirect('/home.html')
        else:
            error_mag = '您的账号或密码错误'
    return render(request, 'login.html', {'error_mag': error_mag})

USER_LIST = [
    {'username':'黄炎','mail':'qq.com','gender':'男'},
]

def home(request):
    if request.method == 'POST':
        u = request.POST.get('username', None)
        m = request.POST.get('mail', None)
        g = request.POST.get('gender', None)
        item = {'username': u, 'mail': m, 'gender': g}
        USER_LIST.append(item)
    return render(request, 'home.html', {'user_list': USER_LIST})

