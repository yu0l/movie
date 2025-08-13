from flask import Flask, request, Response, abort
from flask_httpauth import HTTPBasicAuth
import subprocess
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

# 简单的用户名密码字典
users = {
    "dev": "123456",
    "qa": "654321"
}

@auth.verify_password
def verify(username, password):
    if username in users and users[username] == password:
        return username

# 日志目录（可替换成你自己的路径）
LOG_DIR = r"D:\Projects\movie\movie\account\logs"

@app.route("/logs/<logfile>")
@auth.login_required
def tail_log(logfile):
    if ".." in logfile or "/" in logfile:
        abort(400, "非法路径")


    filepath = os.path.join(LOG_DIR, logfile)
    print(f"{filepath}")
    if not os.path.exists(filepath):
        abort(404, "日志文件不存在")

    # 获取行数参数
    lines = request.args.get("lines", default="500")

    try:
        lines = str(int(lines))
    except:
        lines = "500"

    cmd = ["tail", f"-n{lines}", filepath]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    return Response(output, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
