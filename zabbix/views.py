from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.shortcuts import HttpResponse
import os


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
    {'username':'黄炎','mail':'qq.com','gender':'男','g_list':[],'city':'广州'},
]

def home(request):
    if request.method == 'POST':
        u = request.POST.get('username', None)
        m = request.POST.get('mail', None)
        g = request.POST.get('gender', None)
        city = request.POST.get('city', None)
        g_list = request.POST.getlist('gender1')
        item = {'username': u, 'mail': m, 'gender': g, 'g_list': g_list, 'city':city}
        USER_LIST.append(item)
        pic = request.FILES.get('fafa')
        file_path = os.path.join('static\\image',pic.name )
        with open(file_path,'wb') as f:
            for line in pic.chunks():
                f.write(line)

    return render(request, 'home.html', {'user_list': USER_LIST})

from django.views import View

class Content(View):
    '定于url类的映射'

    def dispatch(self, request, *args, **kwargs):
        result = super(Content, self).dispatch(request, *args, **kwargs)
        return result
    def post(self,request):
        print(request.method)
        return render(request, 'content.html')
    def get(self,request):
        print(request.method)
        return render(request, 'content.html')


user_dict = {
    '1':{'name':'root1','ip':191,'master':'黄炎'},
    '2':{'name':'root2','ip':192,'master':'黄炎'},
    '3':{'name':'root3','ip':193,'master':'黄炎'},
    '4':{'name':'root4','ip':194,'master':'黄炎'}
}

def index(request):
    return render(request,'index.html',{'user_dict':user_dict})

def detail(request, uid):
    # uid = request.GET.get('uid')
    print(uid)
    detail_dict = user_dict[uid]
    return render(request,'detail.html',{'detail_dict':detail_dict})