import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        backlist = ['127.0.0.1', '0.0.0.0']
        # print(request.META)
        print(request.headers)
        return render(request, 'register.html')

    def post(self, request):
        headers = {
            'token': '123456'
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        return HttpResponse(f"恭喜您注册成功，您的账号为{username}账号密码{password}!", headers=headers, status=404)


def header_test(request):
    # data = {
    #     "request.headers": {
    #         "User-Agent": request.headers.get("User-Agent"),
    #         "user-agent": request.headers.get("user-agent"),
    #         "USER-AGENT": request.headers.get("USER-AGENT"),
    #     },
    #     "request.META": {
    #         "HTTP_USER_AGENT": request.META.get("HTTP_USER_AGENT"),
    #         "http_user_agent": request.META.get("http_user_agent"),
    #         "User-Agent": request.META.get("User-Agent"),
    #     }
    # }
    # return JsonResponse(data)
    # data = request.headers
    res = {
        'name': 'ma yue',
        'password': '123456',
    }
    return JsonResponse(res)


def temp_test(request):
    username = 'zhangsan'
    age = 20
    sex = ('男', '女')
    likelist = ["足球","跑步","玩游戏"]
    info = {
        'username': 'zhang_san',
        'password': 123456,
        'email':'766647779@qq.com'
    }
    # info = {}
    # print(info.items())
    # for key, value in info.items():
    #     print(value)

    return render(request, 'test.html',
                  {'name': username, 'age': age, 'sex':sex[0], 'likelist':likelist,'info':info})


def temp_test2(request):
    if 'target' not in request.session:
        request.session['target'] = random.randint(1, 100)
        print(request.session['target'])
        # request.session.modified = True
    message = ""
    if request.method == 'POST':
        try:
            # print(request.session['target'])
            guess = int(request.POST.get("guess"))
            target = request.session.get("target")
            if guess > target:
                message = "你的数字太大了，再试试。"
            elif guess < target:
                message = "你的数字太小了,再试试"
            else:
                message = "恭喜你，猜对了！我又生成了一个新数字。"
                request.session['target'] = random.randint(1, 100)
        except:
            message = "请输入有效的数字"

    return render(request, 'random.html', {'message': message})
