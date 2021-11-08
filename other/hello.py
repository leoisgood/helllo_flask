from flask import Flask, request, render_template

app = Flask(__name__)


# 首页
@app.route('/')  # 接口地址
def index():
    # 接口本身
    return 'home'


# 登录页
@app.route('/login')  # 接口地址
def login():
    # 接口本身
    # 接收请求数据
    username = request.args.get('username')  # 需导入flask的request
    pwd = request.args.get('pwd')
    return f'{username},{pwd}'


# web 服务器
if __name__ == '__main__':
    app.run()

# 重新运行程序，输入网址显示如下图

