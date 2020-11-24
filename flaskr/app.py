from flask import Flask
from flask import request

app = Flask(__name__)


counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = 'runoob'     # 字符串

# print(counter)
# print(miles)
# print(name)


@app.route('/')
def hello_world():
    return '测试'


# @app.route('/hello', methods=['post'])
# def hello():
#     return request.data

# # 随便整点内容
# 在整点内容
# 变成多行的内容


if __name__ == '__main__':
    app.run()
