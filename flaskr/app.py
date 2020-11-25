from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = range(100)  # 字符串
# print(counter)
# print(miles)
print(miles)



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/auth/login')
def login():
    # return render_template('auth/login.html')
    return '登录页面'


@app.route('/hello', methods=['get', 'post'])
def hello():
    return 'hello page'

# # 随便整点内容
# 在整点内容
# 变成多行的内容


if __name__ == '__main__':
    app.run()
