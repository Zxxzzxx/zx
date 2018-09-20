from django.shortcuts import render

# Create your views here.
# 注册
from django.urls import reverse
from django.views import View


class register(View):
    # 注册
    def get(self, request):
        return render(request, 'zx_user/login.html')

    def post(self, request):
        pass


class login(View):
    # 登录
    def post(self, request):
        pass

    def get(self, request):
        pass


class center(View):
    # 个人中心
    def post(self, request):
        pass

    def get(self, request):
        pass


class address(View):
    # 收货地址
    def post(self, request):
        pass

    def get(self, request):
        pass


class info(View):
    # 个人资料
    def post(self, request):
        pass

    def get(self, request):
        pass


class logout(View):
    # 退出
    def post(self, request):
        pass

    def get(self, request):
        pass
