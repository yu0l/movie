from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def login(request):
    # html = """
    # <form>
    # <input name="username">
    # </form>"""
    # return HttpResponse(html)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f"用户名为{username}用户密码{password}")
    else:
        return render(request,'login.html')

class RegisterView(View):
    def get(self,request):
        backlist = ['127.0.0.1','0.0.0.0']
        print(request.META)
        return render(request,'register.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        return HttpResponse(f"恭喜您注册成功，您的账号为{username}账号密码{password}!")