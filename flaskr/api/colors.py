from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)




@app.route('/colors/<palette>/', methods=['post'])
def colors(palette):
    """获取颜色数据对象
    This is using docstrings for specifications.
    ---
    tags:
      - 获取数据
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: 颜色的列表(数据对象)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    all_colors = {
        'cmyk': ['cian', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    # if palette == 'all':
    #     result = all_colors
    # else:
    #     result = {palette: all_colors.get(palette)}

    return jsonify(all_colors)


@app.route('/user/login/', methods=['post'])
def login():
    """ 登入系统
    登录到系统获取颜色.
    ---
    tags:
      - 登入登出
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['全部', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: 颜色的列表(数据对象)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    return '测试login api'


@app.route('/user/loginout/', methods=['post'])
def loginout():
    """ 登出系统
    登录到系统获取颜色.
    ---
    tags:
      - 登入登出
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['全部', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: 颜色的列表(数据对象)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    return '测试loginout api'


@app.route('/user/delete', methods=['delete'])
def deleteUser():
    """ 用户注销
    用户注销账号.
    ---
    tags:
      - 登入登出
    parameters:
      - name: userName
        in: path
        type: string
        required: true
      - name: password
        in: path
        type: string
        required: true
    definitions:
      userName:
        type: string
      password:
        type: string
    responses:
      200:
        description: 删除了对象
        schema:
          $ref: '#/definitions/Palette'
        examples: '注销失败'

    """
    return '测试loginout api'


app.run(debug=True)