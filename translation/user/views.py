from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password, check_password
import re
from .youdao import *
# Create your views here.


def login_views(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        if uname and upwd:
            user = User.objects.filter(uname=uname)
            if user and check_password(upwd, user[0].upassword):
                for i in user:
                    if i.isban == 1:
                        manage = '该用户被禁用'
                        return render(request, 'login.html', locals())
                request.session['uname'] = uname
                return render(request, 'page.html')
            else:
                manage = '用户名或密码输入错误'
                return render(request, 'login.html', locals())
        else:
            manage = '用户名或密码输入错误'
            return render(request, 'login.html', locals())


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST['uname']
        user = User.objects.filter(uname=uname)
        if user:
            manage = '用户名已存在'
            return render(request, 'register.html', locals())
        upwd = request.POST['upwd']
        upassword = make_password(upwd, 'abc', 'pbkdf2_sha1')
        uphone = request.POST['uphone']
        uemail = request.POST['uemail']
        num = re.findall('^1[0-9]{10}', uphone)
        if len(uname) == 0:
            name = '请输入合适的用户名'
            return render(request, 'register.html', locals())
        elif len(upwd) == 0:
            pwd = '请输入合适的密码'
            return render(request, 'register.html', locals())
        elif not num:
            phone = '请输入合适的手机号'
            return render(request, 'register.html', locals())
        else:
            request.session['uname'] = uname
            user = User.objects.create(uname=uname, upassword=upassword,
                                       phone=uphone, email=uemail)
            return render(request, 'page.html')


def page_views(request):
    if request.method == 'GET':
        return render(request, 'page.html')
    else:
        word = request.POST['word']
        select = request.POST['FY']
# TODO
# 根据选择
        if select == 'four':
            if len(word) != 4:
                message = '请输入四字有效成语'
                return render(request, 'page.html', locals())
            else:
                words = youdao(word, len(word))
                uname = request.session['uname']
                History.objects.create(uname=uname, uword=word)
                return render(request, 'page.html', locals())
        elif select == 'five':
            if len(word) != 5:
                message = '请输入五字有效成语'
                return render(request, 'page.html', locals())
            else:
                words = youdao(word, len(word))
                uname = request.session['uname']
                History.objects.create(uname=uname, uword=word)
                return render(request, 'page.html', locals())
        elif select == 'six':
            if len(word) != 6:
                message = '请输入六字有效成语'
                return render(request, 'page.html', locals())
            else:
                words = youdao(word, len(word))
                uname = request.session['uname']
                History.objects.create(uname=uname, uword=word)
                return render(request, 'page.html', locals())
        elif select == 'eight':
            if len(word) != 8:
                message = '请输入八字有效成语'
                return render(request, 'page.html', locals())
            else:
                words = youdao(word, len(word))
                uname = request.session['uname']
                History.objects.create(uname=uname, uword=word)
                return render(request, 'page.html', locals())
        else:
            pass


def history_views(request):
    if request.method == 'GET':
        uname = request.session['uname']
        user = History.objects.filter(uname=uname)
        if not user:
            history = '该用户没有查询记录'
            return render(request, 'history.html', locals())
        else:
            return render(request, 'history.html', locals())
    else:
        uname = request.session['uname']
        user = History.objects.filter(uname=uname)
        user.delete()
        return redirect('/history')
