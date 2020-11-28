from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)




@app.route('/colors/<palette>/', methods=['post'])
def colors(palette):
    """获取颜色数据对象
    This is using docstrings for specifications.
    ---
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


@app.route('/colors/login/', methods=['post'])
def login():
    """登录系统
    登录到系统获取颜色.
    ---
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


app.run(debug=True)