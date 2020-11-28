from flask import Flask, jsonify
from flasgger import Swagger, swag_from
from flask import request
from flask import render_template

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/colors/<palette>/')
def colors(palette):
    # return render_template('auth/login.html')
    return '登录页面'


@app.route('/hello', methods=['get', 'post'])
@swag_from('colors.yml')
def hello():
    return 'hello page'

# # 随便整点内容
# 在整点内容
# 变成多行的内容


if __name__ == '__main__':
    app.run(debug=True)
